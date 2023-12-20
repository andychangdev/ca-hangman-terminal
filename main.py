import inquirer
from pyfiglet import Figlet
from colored import Fore, Style
from game_components.play_hangman import play_hangman
from game_components.wordlist_functions import choose_wordlist, modify_wordlist, create_wordlist
from game_components.wordlist_utilities import prompt_user_options

title = Figlet(font="standard")
print(title.renderText("Hangman"))

def display_menu():
    while True:
        options = ["Play Hangman", "Select Wordlist", "Modify Wordlist", "Create Wordlist", "Exit Program"]
        user_choice = prompt_user_options(options, "Choose an option")
        if user_choice == "Play Hangman":
            play_hangman()
        elif user_choice == "Select Wordlist":
            choose_wordlist()
        elif user_choice == "Modify Wordlist":
            modify_wordlist()
        elif user_choice == "Create Wordlist":
            create_wordlist()
        elif user_choice == "Exit Program":
            print("Thanks for playing! See you next time!")
            break
        else:
            print("\nInvalid selection. Please select a valid option.")

display_menu()