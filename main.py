from wordleSolver.interactiveWordleSolver import interactiveWordleSolver
from utils import get_word_list


def main():
    word_list = get_word_list("words.txt")
    ws = interactiveWordleSolver(word_list)
    ws.solve()


if __name__ == "__main__":
    main()
