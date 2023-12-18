from wordlist_utilities import select_difficulty, select_wordlist


def choose_wordlist():
    selected_difficulty = select_difficulty()
    selected_wordlist_filepath = select_wordlist(selected_difficulty)
    with open("active_wordlist.txt", 'w') as file:
        file.write(selected_wordlist_filepath)
    print(f"Wordlist selected!")
    print(f"\nBack to Main Menu...\n")


