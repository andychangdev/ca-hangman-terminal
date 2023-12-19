from wordlist_utilities import select_difficulty, select_wordlist, edit_wordlist, save_new_wordlist, save_wordlist


def choose_wordlist():
    selected_difficulty = select_difficulty()
    selected_wordlist_filepath = select_wordlist(selected_difficulty)
    with open("active_wordlist.txt", 'w') as file:
        file.write(selected_wordlist_filepath)
    print(f"Wordlist selected!")
    print(f"\nBack to Main Menu...\n")


def modify_wordlist():
    selected_difficulty = select_difficulty()
    wordlist_filepath = select_wordlist(selected_difficulty)
    wordlist = edit_wordlist(wordlist_filepath)
    save_wordlist(wordlist_filepath, wordlist)
    print(f"Back to Main Menu...\n")


def create_wordlist():
    wordlist_folder = select_difficulty()
    wordlist = edit_wordlist(None)
    save_new_wordlist(wordlist_folder, wordlist)
    print(f"Back to Main Menu...\n")