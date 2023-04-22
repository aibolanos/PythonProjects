import random

words = ["python", "programming", "hangman", "game", "turtle"]

word = random.choice(words)
attempts = 6
correct_guesses = set()
incorrect_guesses = set()

while True:
    # Print current state of the game
    display_word = ""
    for letter in word:
        if letter in correct_guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    print(f"Attempts remaining: {attempts}")

    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Check if letter has already been guessed
    if guess in correct_guesses or guess in incorrect_guesses:
        print("You already guessed that letter!")
        continue

    # Check if letter is in the word
    if guess in word:
        correct_guesses.add(guess)
        print("Correct!")
    else:
        incorrect_guesses.add(guess)
        attempts -= 1
        print("Incorrect!")

    # Check if player has won or lost
    if correct_guesses == set(word):
        print(f"You won! The word was {word}.")
        break
    elif attempts == 0:
        print(f"You lost! The word was {word}.")
        break

