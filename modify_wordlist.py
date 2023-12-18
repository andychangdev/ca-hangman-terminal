import os
import inquirer
from wordlist_utilities import select_difficulty, select_wordlist


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


def edit_wordlist(filepath):
    if filepath:
        wordlist = load_wordlist(filepath)
        if wordlist:
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
    

def modify_wordlist():
    selected_difficulty = select_difficulty()
    wordlist_filepath = select_wordlist(selected_difficulty)
    wordlist = edit_wordlist(wordlist_filepath)
    save_wordlist(wordlist_filepath, wordlist)