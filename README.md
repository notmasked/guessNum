# GuessNum

GuessNum is a command-line number guessing game written in Python. The computer randomly selects a number between 1 and 100, and your goal is to guess it in as few attempts as possible. The game keeps track of your best score across sessions using a text file.

## Features

* Random number generation
* Hints after every guess (Higher/Lower)
* Persistent best score tracking
* Main menu navigation
* Play Again option
* Basic input validation

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the source code.
3. Ensure `bestscore.txt` is present in the project directory.
4. Open a terminal in the project folder.
5. Run:

```bash
python main.py
```

## Gameplay

* The computer selects a random number between **1 and 100**.
* Enter your guesses until you find the correct number.
* After each incorrect guess, you'll receive a hint:

  * **Higher** if your guess is too low.
  * **Lower** if your guess is too high.
* If you beat your previous best score, it is automatically saved.

## Files

* `main.py` – Game logic
* `bestscore.txt` – Stores the lowest number of guesses required to win

## Author

**Harshad Sawant**

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
