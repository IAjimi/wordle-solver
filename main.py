from tqdm import tqdm
import pandas as pd
import numpy as np

from typing import List, Tuple

from constants import (
    NOT_IN_WORD,
    WRONG_POS,
    CORRECT_POS,
    CORRECT_WORD,
    MAX_GUESSES,
    INITIAL_GUESS,
)
from utils import get_word_list


def get_guess_response(word: str, correct_word: str) -> List[int]:
    guess_response = []
    for ix, letter in enumerate(word):
        if letter in correct_word:
            if letter == correct_word[ix]:
                guess_response.append(CORRECT_POS)
            else:
                guess_response.append(WRONG_POS)
        else:
            guess_response.append(NOT_IN_WORD)

    return guess_response


def filter_words(
    letter: str, guess_pos: int, response: int, word_array: np.array
) -> pd.DataFrame:
    """Filter word_array based on one letter response."""
    if response == NOT_IN_WORD:
        filter_func = np.vectorize(lambda x: letter not in x)
    elif response == WRONG_POS:
        filter_func = np.vectorize(lambda x: letter in x and x[guess_pos] != letter)
    elif response == CORRECT_POS:
        filter_func = np.vectorize(lambda x: x[guess_pos] == letter)
    else:
        raise Exception(f"Unknown response {response}.")

    filter_bool = filter_func(word_array)
    return word_array[filter_bool]


def process_response(word: str, response_list: List[int], word_array: np.array):
    for ix, letter in enumerate(word):
        word_array = filter_words(letter, ix, response_list[ix], word_array)
    return word_array


def main(word_array: np.array, correct_word: str) -> Tuple[bool, int]:
    guess = INITIAL_GUESS  # hardcoding an initial guess

    for attempt in range(MAX_GUESSES):
        guess_response = get_guess_response(guess, correct_word)
        if guess_response == CORRECT_WORD:
            return True, attempt
        else:
            word_array = process_response(guess, guess_response, word_array)
            if len(word_array) == 0:
                print(f"There are no available words left to guess.")
                return False, MAX_GUESSES

        guess = word_array[0]

    return False, MAX_GUESSES


def simulate_puzzles(
    word_list: List[str], word_array: np.array
) -> Tuple[int, List[int]]:
    wins = 0
    attempts = []
    for word in tqdm(word_list):
        w, a = main(word_array, word)
        wins += w
        if w:
            attempts.append(a)

    return wins, attempts


if __name__ == "__main__":
    print("Getting word list...")
    word_list = get_word_list("words.txt")

    print("Simulating solving puzzles...")
    word_array = np.array(word_list)
    wins, attempts = simulate_puzzles(word_list, word_array)

    print(f"The solver found {wins} correct words out of a list of {len(word_list)}.")
    print(
        f"The correct answer was found in a median number of {np.median(attempts):.2f} attempts."
    )
