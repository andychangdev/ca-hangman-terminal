import inquirer
from colored import Fore, Style
from play_hangman import play_hangman
from wordlist_functions import choose_wordlist, modify_wordlist, create_wordlist
from wordlist_utilities import prompt_user_options


print(f"\n{Fore.cyan}Welcome to Hangman!{Style.reset}\n")

def display_menu():
    while True:
        options = ["Play Hangman", "Select Wordlist", "Modify Wordlist", "Create Wordlist", "Exit"]
        user_choice = prompt_user_options(options)
        if user_choice == "Play Hangman":
            play_hangman()
        elif user_choice == "Select Wordlist":
            choose_wordlist()
        elif user_choice == "Modify Wordlist":
            modify_wordlist()
        elif user_choice == "Create Wordlist":
            create_wordlist()
        elif user_choice == "Exit":
            print("Thanks for playing! See you next time!")
            break
        else:
            print("\nInvalid selection. Please select a valid option.")

display_menu()