from typing import List


from constants import WORD_LENGTH


def get_word_list(filename: str) -> List[str]:
    """Returns list of words meeting the Wordle criteria."""
    with open(filename) as f:
        word_list = f.read().splitlines()

    word_list = filter_word_list(word_list)
    return word_list


def filter_word_list(word_list: List[str]) -> List[str]:
    """Filter list of words to words suitable for wordle."""
    suitable_words = [word for word in word_list if len(word) == WORD_LENGTH]
    return suitable_words
