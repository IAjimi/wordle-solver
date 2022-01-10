import abc

import numpy as np
import random

from typing import List, Tuple

from constants import (
    NOT_IN_WORD,
    WRONG_POS,
    CORRECT_POS,
    CORRECT_WORD,
    MAX_GUESSES,
)
from exceptions import OutOfWords


class wordleSolver:
    def __init__(self, word_list: List[str], verbose: bool = False):
        self.words = np.array(word_list)
        self.verbose = verbose

    def guess_word(self, word_array: np.array) -> str:
        """Return guess based on remaining words."""
        return random.choice(word_array)

    def filter_words(
        self, letter: str, guess_pos: int, response: int, word_array: np.array
    ) -> Tuple[np.array, np.array]:
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

    def process_response(
        self, word: str, response_list: List[int], word_array: np.array
    ) -> np.array:
        """Iteratively filter word_array based on a full guess."""
        for ix, letter in enumerate(word):
            if len(word_array) > 0:
                word_array = self.filter_words(
                    letter, ix, response_list[ix], word_array
                )
            else:
                raise OutOfWords
        return word_array

    @abc.abstractmethod
    def get_guess_response(self, guess: str) -> List[int]:
        """Returns a list of responses (must be either NOT_IN_WORD, WRONG_POS, or CORRECT_POS)."""
        raise NotImplementedError

    def solve(self) -> Tuple[bool, int]:
        word_array = self.words.copy()

        for attempt in range(MAX_GUESSES):
            guess = self.guess_word(word_array)
            if self.verbose:
                print(f"Guess: {guess}")
            guess_response = self.get_guess_response(guess)
            if guess_response == CORRECT_WORD:
                return True, attempt
            else:
                word_array = self.process_response(guess, guess_response, word_array)

        return False, MAX_GUESSES
