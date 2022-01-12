from typing import List

import numpy as np

from .constants import WORD_LENGTH, NOT_IN_WORD, CORRECT_POS, WRONG_POS
from .wordleSolver import wordleSolver


class interactiveWordleSolver(wordleSolver):
    def __init__(self, word_list: List[str]):
        super().__init__(word_list, verbose=True)
        self.VALID_INPUTS = [NOT_IN_WORD, WRONG_POS, CORRECT_POS]

    def print_guess_instructions(self, guess: str, APPROVED_GUESS: str, DENIED_GUESS: str) -> None:
        """Print instructions for users when being proposed a guess."""
        print(f"Your suggested guess is {guess}.")
        print(f"Type '{APPROVED_GUESS}' to confirm and '{DENIED_GUESS}' to pick another word.")

    def validate_guess(self, word_array: np.array, guess: str) -> str:
        """Allows for the user to choose a different guess."""
        APPROVED_GUESS = "yes"
        DENIED_GUESS = "no"

        self.print_guess_instructions(guess, APPROVED_GUESS, DENIED_GUESS)
        confirm = input()

        while confirm != APPROVED_GUESS:
            if confirm == DENIED_GUESS:
                guess = self.guess_word(word_array)
                self.print_guess_instructions(guess, APPROVED_GUESS, DENIED_GUESS)
                confirm = input()
            else:
                self.print_guess_instructions(guess, APPROVED_GUESS, DENIED_GUESS)
                confirm = input()

        return guess

    def print_user_input_instructions(self) -> None:
        print("Enter the puzzle's feedback as follows:")
        print("0 if the letter was grey.")
        print("1 if the letter was orange.")
        print("2 if the letter was green.")

        print(
            "For example, a grey-orange-green-grey-grey sequence should be entered as 01200."
        )

    def get_user_input(self) -> List[int]:
        """Read and parse user input."""
        response = input()
        parsed_response = [int(i) for i in response if int(i) in self.VALID_INPUTS]
        return parsed_response

    def get_guess_response(self, guess: str) -> List[int]:
        """Returns a list of responses (must be either NOT_IN_WORD, WRONG_POS, or CORRECT_POS)."""
        self.print_user_input_instructions()

        parsed_response = self.get_user_input()

        while len(parsed_response) != WORD_LENGTH:
            print("Invalid response. Please retry.")
            parsed_response = self.get_user_input()

        return parsed_response
