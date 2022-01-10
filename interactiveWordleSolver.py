from typing import List

from constants import WORD_LENGTH, NOT_IN_WORD, CORRECT_POS, WRONG_POS
from wordleSolver import wordleSolver


class interactiveWordleSolver(wordleSolver):
    def __init__(self, word_list: List[str]):
        super().__init__(word_list, verbose=True)
        self.VALID_INPUTS = [NOT_IN_WORD, WRONG_POS, CORRECT_POS]

    def print_user_input_instructions(self) -> None:
        print("Enter the puzzle's feedback as follows:")
        print("0 if the letter was grey.")
        print("1 if the letter was orange.")
        print("2 if the letter was green.")

        print(
            "For example, a grey-orange-green-grey-grey sequence should be entered as 01200."
        )

    def get_user_input(self) -> List[int]:
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
