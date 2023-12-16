import random


def get_wordlist():
    with open("wordlist.txt", "r") as file:
        words = file.read().splitlines()
    return words


def random_word_generator(word_list):
    return random.choice(word_list)


def input_guess(available_letters, secret_letters, lives):
    while True:
        try:
            user_guess = input("\nGuess a letter: ")
            if not user_guess.isalpha():
                raise Exception("\nYou must guess a letter!")
            elif len(user_guess) != 1:
                raise Exception("\nYou must only guess one letter at a time!")
            elif user_guess not in available_letters:
                raise Exception("\nYou've guessed that letter already!")
            else:
                break
        except Exception as error:
            print(error)

    if user_guess not in secret_letters.values():
        lives -= 1
        if lives > 0:
            print(f"\nYour guess is incorrect! You only have {lives} lives left.\n")
    return user_guess, lives


def play_hangman():
    words = get_wordlist()
    secret_word = random_word_generator(words)
    secret_letters = {}
    for index, letter in enumerate(secret_word):
        secret_letters[index] = letter

    print(f"\nWelcome to Hangman!\n")
    print(f"\nYour word is {len(secret_letters)} letters long.")
    print(secret_word)
    print(secret_letters)
    user_progress = ["_"] * len(secret_letters)
    print(" ".join(user_progress))
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    lives = 7
    user_guess, lives = input_guess(available_letters, secret_letters, lives)
    print(user_guess)
    print(lives)


play_hangman()
