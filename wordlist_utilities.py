import os
import inquirer


def select_difficulty():
    prompt = [
        inquirer.List(
            "choice",
            message="Select a difficulty level",
            choices=["Easy", "Medium", "Hard"],
        ),
    ]
    try:
        selections = inquirer.prompt(prompt)
        user_choice = selections["choice"]
        return user_choice.lower()
    except KeyError as error:
        print(f"Error: Invalid choice - {error}")
        return None


def select_wordlist(difficulty):
    folder_path = os.path.join("wordlists", difficulty)
    try:
        wordlists = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Directory '{folder_path}' not found.")
        return None

    choices = wordlists
    questions = [
        inquirer.List(
            "wordlist",
            message="Select a wordlist",
            choices=choices,
        ),
    ]
    try:
        answers = inquirer.prompt(questions)
        selected_wordlist = answers["wordlist"]
        wordlist_filepath = os.path.join(folder_path, selected_wordlist)
        return wordlist_filepath
    except KeyError as error:
        print(f"Error: Invalid choice - {error}")
        return None
    

def prompt_user(instructions):
    while True:
        try:
            prompt = [inquirer.Text("input", message=instructions)]
            answer = inquirer.prompt(prompt)
            user_input = answer["input"]
            if " " in user_input:
                raise ValueError("Invalid input. Name must not contain spaces.")
            elif not user_input.isalpha():
                raise ValueError("Invalid input. Name must only alphabet letters")
            elif len(user_input) < 4:
                raise ValueError("Invalid input. Name must contain atleast 4 letters")
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
    print(f'Wordlist saved in "{filepath}"\n')


def save_new_wordlist(wordlist_name, wordlist_folder, wordlist):
    filename = f"{wordlist_name}.txt"
    folder_path = os.path.join('wordlists', wordlist_folder)
    wordlist_filepath = os.path.join(folder_path, filename)
    save_wordlist(wordlist_filepath, wordlist)

    
def edit_wordlist(filepath):
    if filepath:
        wordlist = load_wordlist(filepath)
    else:
        wordlist = []

    while True:
        prompt = [
            inquirer.List(
                "choice",
                message="Select an option",
                choices=["Add Word", "Remove Word", "View Wordlist", "Save and Exit"],
            ),
        ]
        
        selections = inquirer.prompt(prompt)
        user_choice = selections["choice"]
        if user_choice == "Add Word":
            word = input("Enter the word to add: ")
            wordlist.append(word)
            print(f'\n"{word}" added to wordlist\n')
        elif user_choice == "Remove Word":
            word = input("Enter the word to remove: ")
            if word in wordlist:
                wordlist.remove(word)
                print(f'\n"{word}" removed from wordlist\n')
            else:
                print("Word not found in the list.")
        elif user_choice == "View Wordlist":
            print("Wordlist:\n")
            display_wordlist_characters(wordlist, 100)
            print()
        elif user_choice == "Save and Exit":
            return wordlist
        else:
            print("\nInvalid selection. Please select a valid option.")