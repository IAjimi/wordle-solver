from typing import List


from constants import WORD_LENGTH


def get_word_list(filename: str) -> List[str]:
    """Returns list of words of the right length."""
    with open(filename) as f:
        word_list = f.read().splitlines()

    word_list = [word for word in word_list if len(word) == WORD_LENGTH]
    return word_list
