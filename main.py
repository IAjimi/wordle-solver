"""
List of words comes from http://www.mieliestronk.com/corncob_lowercase.txt

This solver's strategy is extremely simple:
    * pick the first remaining word available as a guess
    * filter the list of remaining words based on the response given
        (
            0 -> the letter isn't in the word
            1 -> the letter is in the word but in a different position
            2 -> the letter is in the correct position
        )

This approach solves > 95% of puzzles for this word list.
"""

from tqdm import tqdm
import pandas as pd
import numpy as np

from typing import List, Tuple

from constants import (
    NOT_IN_WORD,
    WRONG_POS,
    CORRECT_POS,
    NOT_IN_WORD_IX,
    CORRECT_WORD,
    MAX_GUESSES,
)
from utils import get_word_list, create_word_dataframe


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
    letter: str, guess_pos: int, response: int, word_df: pd.DataFrame
) -> pd.DataFrame:
    """Filter word_df based on one letter response."""
    if response == NOT_IN_WORD:
        word_df = word_df.loc[word_df[letter] == NOT_IN_WORD_IX]
    elif response == WRONG_POS:
        word_df = word_df.loc[
            (word_df[letter] != NOT_IN_WORD_IX) & (word_df[letter] != guess_pos)
        ]
    elif response == CORRECT_POS:
        word_df = word_df.loc[word_df[letter] == guess_pos]
    else:
        raise Exception(f"Unknown response: {response}.")

    return word_df


def process_response(word: str, response_list: List[int], word_df: pd.DataFrame):
    for ix, letter in enumerate(word):
        word_df = filter_words(letter, ix, response_list[ix], word_df)
    return word_df


def main(word_df: pd.DataFrame, correct_word: str) -> Tuple[bool, int]:
    for attempt in range(MAX_GUESSES):
        guess = word_df.index[0]  # the first word left in word_df
        guess_response = get_guess_response(guess, correct_word)
        if guess_response == CORRECT_WORD:
            return True, attempt
        else:
            word_df = process_response(guess, guess_response, word_df)
            if word_df.empty:
                print(f"There are no available words left to guess.")
                return False, MAX_GUESSES

    return False, MAX_GUESSES

def simulate_puzzles(word_list: List[str], word_df: pd.DataFrame) -> Tuple[int, List[int]]:
    wins = 0
    attempts = []
    for word in tqdm(word_list):
        w, a = main(word_df, word)
        wins += w
        if w:
            attempts.append(a)

    return wins, attempts


if __name__ == "__main__":
    print("Getting word list...")
    word_list = get_word_list("words.txt")
    word_df = create_word_dataframe(word_list)

    print("Simulating solving puzzles...")
    wins, attempts = simulate_puzzles(word_list, word_df)

    print(f"The solver found {wins} correct words out of a list of {len(word_list)}.")
    print(
        f"The correct answer was found in a median number of {np.median(attempts):.2f} attempts."
    )
