## Wordle Solver
[Wordle](https://www.powerlanguage.co.uk/wordle/) is a daily word game.

Players have 6 tries to find a five letter English word.

After each guess, the player receives a response for every letter in their guess:
* Grey: the letter isn't in the word
* Orange: the letter is in the word but in a different position
* Green: the letter is in the correct position

The code is in Python repository solves Wordle-like puzzles with an extremely simple strategy:
* pick "early" as the 1st guess (a personal heuristic)
* filter the list of remaining words based on the response given
* subsequently pick the first word available as a guess

using a list of words found at http://www.mieliestronk.com/corncob_lowercase.txt.

It turns out that this approach solves > 90% of puzzles for this word list.

Future iterations of this project may attempt to find the word using the least amount of tries possible.
The project could also be extended to allow people to play the game using the CLI.