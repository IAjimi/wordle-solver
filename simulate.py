from tqdm import tqdm
import numpy as np

from typing import List, Tuple

from simulatedWordleSolver import simulatedWordleSolver
from utils import get_word_list


def simulate_puzzles(
    word_list: List[str],
) -> Tuple[int, List[int]]:

    wins = 0
    attempts = []

    for word in tqdm(word_list):
        ws = simulatedWordleSolver(word_list, word)
        won, attempt_count = ws.solve()
        wins += won
        attempts.append(attempt_count)

    return wins, attempts


def print_statistics(wins: int, attempts: List[int]) -> None:
    print(f"Solved: {wins} / {len(word_list)}")
    print(f"Accuracy: {wins / len(word_list):.2%}")
    print(f"Average # of attempts: {np.mean(attempts):.2f}")
    print(f"Median # of attempts: {np.median(attempts):.2f}")


if __name__ == "__main__":
    print("Getting word list...")
    word_list = get_word_list("words.txt")

    print("Simulating puzzles...")
    wins, attempts = simulate_puzzles(word_list)
    print_statistics(wins, attempts)
