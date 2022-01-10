from typing import List

from constants import NOT_IN_WORD, CORRECT_POS, WRONG_POS
from wordleSolver import wordleSolver


class simulatedWordleSolver(wordleSolver):
    def __init__(self, word_list: List[str], correct_word: str):
        super().__init__(word_list)
        self.correct_word = correct_word

    def get_guess_response(self, guess: str) -> List[int]:
        """Returns a list of responses (must be either NOT_IN_WORD, WRONG_POS, or CORRECT_POS)."""
        guess_response = []
        for ix, letter in enumerate(guess):
            if letter not in self.correct_word:
                guess_response.append(NOT_IN_WORD)
            elif letter != self.correct_word[ix]:
                guess_response.append(WRONG_POS)
            else:
                guess_response.append(CORRECT_POS)

        return guess_response
