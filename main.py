import inquirer
from play_hangman import play_hangman
from wordlist_functions import choose_wordlist, modify_wordlist, create_wordlist


print("\nWelcome to Hangman!\n")

def display_menu():
    while True:
        prompt = [
            inquirer.List(
                "choice",
                message="Choose an option",
                choices=["Play Hangman", "Select Wordlist", "Modify Wordlist", "Create Wordlist", "Exit"],
            ),
        ]
        selections = inquirer.prompt(prompt)
        user_choice = selections["choice"]

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