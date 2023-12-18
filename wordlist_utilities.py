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
    except KeyError as e:
        print(f"Error: Invalid choice - {e}")
        return None