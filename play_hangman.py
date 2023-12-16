import random

def get_wordlist():
    with open("wordlist.txt", "r") as file:
        words = file.read().splitlines()
    return words

def random_word_generator(word_list):
    return random.choice(word_list)

def play_hangman():
    words = get_wordlist()
    secret_word = random_word_generator(words)
    secret_letters = {}
    for index, letter in enumerate(secret_word):
        secret_letters[index] = letter

    print(f"\nWelcome to Hangman!\n")
    print(f"\nYour word is {len(secret_letters)} letters long.")
    print (secret_word)
    print (secret_letters)

play_hangman()