# Number Guessing Game & Word Counter

A Python terminal program built for my Python internship practice. It brings two small utilities together under one start menu: a 1–100 number guessing game and a text file word frequency counter.

## Background & How I Built It

I built this as a combined practice script after working on basic Python programs like a calculator. Instead of keeping separate mini-scripts scattered around, I wanted one menu-driven program where I could practice input validation, loops, file reading, and standard library modules.

While putting it together, I checked the official Python documentation for `random.randint` and `collections.Counter`, watched/read a few basic walkthroughs on handling `FileNotFoundError` and `ValueError` in Python, and tested edge cases like non-number guesses, out-of-range numbers, missing files, and sample text (including public-domain text like `sample.txt`). I wrote and edited the code in VS Code and ran it from the terminal to check how each option behaves.

## What You Need
- **Python 3.10+** (only built-in modules are used: `random`, `string`, and `collections`—no external packages to install)
- **VS Code** or any text editor/terminal to run the script
- A text file named `sample.txt` in the project folder if you want to test the default word counter input right away

## How to Run
1. Open your terminal in the project folder.
2. Run the program with:
   ```bash
   py main.py or python main.py depending on your system configuration
