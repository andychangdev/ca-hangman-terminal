import os
import inquirer
from colored import Fore, Style


def select_difficulty():
    prompt = [
        inquirer.List(
            "choice",
            message="Select a difficulty level",
            choices=["Easy", "Medium", "Hard"],
        ),
    ]
    selections = inquirer.prompt(prompt)
    user_choice = selections["choice"]
    return user_choice.lower()


def select_wordlist(difficulty):
    folder_path = os.path.join("wordlists", difficulty)
    wordlists = os.listdir(folder_path)

    choices = wordlists
    questions = [
        inquirer.List(
            "wordlist",
            message="Select a wordlist",
            choices=choices,
        ),
    ]
    answers = inquirer.prompt(questions)
    selected_wordlist = answers["wordlist"]
    wordlist_filepath = os.path.join(folder_path, selected_wordlist)
    return wordlist_filepath


def prompt_user_options(options, instructions):
    prompt = [
            inquirer.List(
                "choice",
                message=instructions,
                choices=options,
            ),
        ]
    selections = inquirer.prompt(prompt)
    user_choice = selections["choice"]
    return user_choice


def prompt_user_input(type, instructions):
    while True:
        try:
            prompt = [inquirer.Text("input", message=instructions)]
            answer = inquirer.prompt(prompt)
            user_input = answer["input"]
            if " " in user_input:
                raise ValueError(f"{Fore.red}Error: {type} must not contain spaces.{Style.reset}\n")
            elif not user_input.isalpha():
                raise ValueError(f"{Fore.red}Error: {type} must only use alphabet letters.{Style.reset}\n")
            elif len(user_input) < 4:
                raise ValueError(f"{Fore.red}Error: {type} must contain atleast 4 letters.{Style.reset}\n")
            else:
                return user_input.lower()
        except ValueError as error:
            print(error)


def display_wordlist_characters(wordlist, chars_per_line):
    current_line_length = 0

    for word in wordlist:
        if current_line_length + len(word) + 1 <= chars_per_line:
            print(word, end=" ")
            current_line_length += len(word) + 1
        else:
            print()
            print(word, end=" ")
            current_line_length = len(word) + 1
    print()


def load_wordlist(filepath):
    with open(filepath, "r") as file:
        words = file.read().splitlines()
    return words


def save_wordlist(filepath, wordlist):
    with open(filepath, "w") as file:
        file.write("\n".join(wordlist))


def save_new_wordlist(wordlist_folder, wordlist):
    folder_path = os.path.join('wordlists', wordlist_folder)
    existing_wordlists = os.listdir(folder_path)
    while True:
        wordlist_name = prompt_user_input("Wordlist name", "Enter a name for your wordlist")
        filename = f"{wordlist_name}.txt"
        try:
            if filename in existing_wordlists:
                raise ValueError (f"{Fore.red}Error: The wordlist '{wordlist_name}' already exists.{Style.reset}\n")
            else:
                wordlist_filepath = os.path.join(folder_path, filename)
                save_wordlist(wordlist_filepath, wordlist)
                break
        except ValueError as error:
                    print(error)

    
def edit_wordlist(filepath):
    if filepath:
        wordlist = load_wordlist(filepath)
    else:
        wordlist = []

    while True:
        options = ["Add Word", "Remove Word", "View Wordlist", "Save and Exit"]
        user_choice = prompt_user_options(options, "Choose an option")
        if user_choice == "Add Word":
            while True:
                try:
                    word = prompt_user_input("Word", "Enter a word to add (or enter 'quit' to stop adding)")
                    if word in wordlist:
                        raise ValueError (f"{Fore.red}Error: '{word}' already exists in wordlist.{Style.reset}\n")
                    if word == "quit":
                        break
                    else:
                        wordlist.append(word)
                        print(f"{Fore.green}'{word}' added to wordlist.{Style.reset}\n")
                except ValueError as error:
                    print(error)
        elif user_choice == "Remove Word":
            while True:
                try:
                    word = prompt_user_input("Word", "Enter a word to remove (or enter 'quit' to stop removing)")
                    if word == "quit":
                        break
                    if word not in wordlist:
                        raise ValueError (f"{Fore.red}Error: '{word}' not found in wordlist.{Style.reset}\n")
                    else:
                        wordlist.remove(word)
                        print(f"{Fore.orange_1}'{word}' removed from wordlist{Style.reset}\n")
                except ValueError as error:
                    print(error)
        elif user_choice == "View Wordlist":
            print(f"{Fore.cyan}Current Wordlist:\n{Style.reset}")
            display_wordlist_characters(wordlist, 100)
            print()
        elif user_choice == "Save and Exit":
            if (len(wordlist)) < 10:
                print(f"{Fore.red}Error: Wordlist must contain atleast 10 words.{Style.reset}\n")
            else: 
                return wordlist
        else:
            print(f"\n{Fore.red}Error: Invalid selection. Please select a valid option.{Style.reset}")