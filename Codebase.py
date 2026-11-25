import random

# List of words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
secret_word = "python"  # Fixed word for testing
# secret_word = random.choice(words)  # For random word

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nProgress:", display_word)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("You won! The word was", secret_word)
        print("Wrong guesses:", wrong_guesses, "/6")
        break

    guess = input("Enter a letter: ").lower().strip()

    # Check invalid input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed", guess,
              "Try another letter. (no attempt lost)")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print(guess, ": Correct")
    else:
        wrong_guesses += 1
        print("Wrong guess (", wrong_guesses, "/6)")

# Game over condition
if wrong_guesses == max_attempts:
    print("\nGame Over! The word was", secret_word)
