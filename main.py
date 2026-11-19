import random
import string
from collections import Counter


def play_guessing_game(best_score=0):
    """Play a 1-to-100 guessing game with attempts, scoring, best score, and replay."""
    low = 1
    high = 100
    max_attempts = 7

    while True:
        # Pick the secret number once before each round starts
        secret = random.randint(low, high)
        attempts_used = 0
        wrong_guesses = 0
        won = False

        print(f"\nGuess a number between {low} and {high}. You have {max_attempts} attempts.")

        while attempts_used < max_attempts:
            raw_guess = input(f"Attempt {attempts_used + 1}/{max_attempts} - Enter a whole number: ").strip()

            # Reject non-integer input without crashing or burning an attempt
            try:
                guess = int(raw_guess)
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if guess < low or guess > high:
                print(f"Please enter a number between {low} and {high}.")
                continue

            attempts_used += 1

            if guess < secret:
                print("Too low.")
                wrong_guesses += 1
            elif guess > secret:
                print("Too high.")
                wrong_guesses += 1
            else:
                print(f"Correct! You guessed {secret} in {attempts_used} attempt(s).")
                won = True
                break

        if not won:
            print(f"Out of attempts! The secret number was {secret}.")

        score = max(0, 100 - 10 * wrong_guesses) if won else 0
        if score > best_score:
            best_score = score

        print(f"Attempts used: {attempts_used}/{max_attempts} | Score: {score} | Best score: {best_score}")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    return best_score


def count_words_in_file(file_path="sample.txt", top_n=10):
    """Read a text file safely, clean text, and print word counts and top words."""
    try:
        with open(file_path, encoding="utf-8") as file:
            raw_text = file.read()
    except FileNotFoundError:
        print(f"Could not find '{file_path}'. Make sure the file exists and try again.")
        return

    # Normalize case, strip punctuation via str.translate, split into words, and count
    cleaned_text = raw_text.lower().translate(str.maketrans("", "", string.punctuation))
    words = cleaned_text.split()
    counts = Counter(words)

    total_words = sum(counts.values())
    unique_words = len(counts)

    print(f"\nFile: {file_path}")
    print(f"Total words:  {total_words}")
    print(f"Unique words: {unique_words}")

    if total_words == 0:
        print("No words found in the file.")
        return

    print(f"\nTop {min(top_n, unique_words)} words:")
    print(f"{'Word':<15} {'Count':>6}")
    print("-" * 22)
    for word, count in counts.most_common(top_n):
        print(f"{word:<15} {count:>6}")


def main():
    """Main menu to switch between the guessing game, word counter, and exit."""
    best_score = 0

    while True:
        print("\n=== Start Menu ===")
        print("1. Play the game")
        print("2. Count words in a file")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            best_score = play_guessing_game(best_score)
        elif choice == "2":
            user_path = input("Enter file path (press Enter for 'sample.txt'): ").strip()
            target_path = user_path if user_path else "sample.txt"
            count_words_in_file(target_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()