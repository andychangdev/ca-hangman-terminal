import random
from colored import Fore, Style
from wordlist_utilities import prompt_user_options, load_wordlist


def get_active_wordlist():
    with open("active_wordlist.txt", "r") as active_file:
        active_wordlist = active_file.read()
    words = load_wordlist(active_wordlist)
    return words


def random_word_generator(wordlist):
    return random.choice(wordlist)


def input_guess(available_letters, secret_letters, lives):
    while True:
        try:
            user_guess = input("\nGuess a letter: ")
            if not user_guess.isalpha():
                raise ValueError(f"\n{Fore.red}You must guess a letter!{Style.reset}")
            elif len(user_guess) != 1:
                raise ValueError(f"\n{Fore.red}You must only guess one letter at a time!{Style.reset}")
            elif user_guess not in available_letters:
                raise ValueError(f"\n{Fore.red}You've guessed that letter already!{Style.reset}")
            else:
                break
        except ValueError as error:
            print(error)

    if user_guess not in secret_letters.values():
        lives -= 1
        if lives > 0:
            print(f"\n{Fore.orange_1}Your guess is incorrect! You only have {lives} lives left.{Style.reset}\n")
    return user_guess, lives


def update_progress(user_progress, secret_letters, user_guess):
    guess = False
    for position, letter in secret_letters.items():
        if user_guess == letter:
            user_progress[position] = letter
            guess = True
    if guess:
        print(f"\n{Fore.green}Your guess is correct!{Style.reset}\n")
    print(" ".join(user_progress))
    return user_progress


def update_available_letters(user_guess, available_letters):
    available_letters = available_letters.replace(user_guess, "")
    return available_letters


def play_hangman():
    words = get_active_wordlist()
    secret_word = random_word_generator(words)
    secret_letters = {}
    for index, letter in enumerate(secret_word):
        secret_letters[index] = letter
        
    print(f"{Fore.cyan}Objective: Guess the hidden word before making too many incorrect guesses.{Style.reset}")
    print(f"\nYour word is {len(secret_letters)} letters long.")
    user_progress = ["_"] * len(secret_letters)
    print(" ".join(user_progress))
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    lives = 7

    while "_" in user_progress:
        user_guess, lives = input_guess(available_letters, secret_letters, lives)
        user_progress = update_progress(user_progress, secret_letters, user_guess)
        available_letters = update_available_letters(user_guess, available_letters)
        print(f"\nAvailable letters:\n{available_letters}")

        if "".join(user_progress) == secret_word:
            print(f"\n{Fore.cyan}Congratulations! You have guessed the hidden word! You win!{Style.reset}")
            break
        if lives == 0:
            print(f"\n{Fore.cyan}You are out of lives! You lose!\nThe hidden word was {secret_word.capitalize()}!{Style.reset}\n")
            break

    while True:
        play_again = ["Yes", "No"]
        user_choice = prompt_user_options(play_again, "Do you want to play again")
        if user_choice == "Yes":
            play_hangman()
            break
        elif user_choice == "No":
            print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")
            break
        else:
            print(f"\n{Fore.red}Error: Please selection a valid option (yes/no).{Style.reset}")