from typing import List

from collections import Counter

import string
import pandas as pd

from constants import NOT_IN_WORD_IX, WORD_LENGTH


def get_word_list(filename: str) -> List[str]:
    """Returns list of words meeting the Wordle criteria."""
    with open(filename) as f:
        word_list = f.read().splitlines()

    word_list = filter_word_list(word_list)
    return word_list


def is_suitable(word: str) -> bool:
    """Returns True if a word is suitable for wordle,
    i.e., 5 letter words where each letter appears at most once."""
    if len(word) == WORD_LENGTH:
        letter_frequency = Counter(word).values()
        if max(letter_frequency) == 1:
            return True
    return False


def filter_word_list(word_list: List[str]) -> List[str]:
    """Filter list of words to words suitable for wordle."""
    suitable_words = [word for word in word_list if is_suitable(word)]
    return suitable_words


def create_word_dataframe(word_list: List[str]) -> pd.DataFrame:
    """Create a DataFrame where the index is a word and the columns
    are the positions of a letter in the word. If the letter isn't
    found in the word, the position is marked as -1.

    For ex:
           a  b  c  d  e ...  x  y  z
    early  1 -1 -1 -1  0 ... -1  4 -1

    """
    letters = list(string.ascii_lowercase)
    word_df = pd.DataFrame(NOT_IN_WORD_IX, index=word_list, columns=letters)

    for word in word_list:
        for letter_pos, letter in enumerate(word):
            word_df.loc[word, letter] = letter_pos

    return word_df
