from colored import Fore, Style
from game_components.wordlist_utilities import select_difficulty, select_wordlist, edit_wordlist, save_new_wordlist, save_wordlist


def choose_wordlist():
    selected_difficulty = select_difficulty()
    selected_wordlist_filepath = select_wordlist(selected_difficulty)
    with open("active_wordlist.txt", 'w') as file:
        file.write(selected_wordlist_filepath)
    print(f"{Fore.green}Wordlist selected!{Style.reset}")
    print(f"\n{Fore.cyan}Back to Main Menu...{Style.reset}\n")


def modify_wordlist():
    selected_difficulty = select_difficulty()
    wordlist_filepath = select_wordlist(selected_difficulty)
    wordlist = edit_wordlist(wordlist_filepath)
    save_wordlist(wordlist_filepath, wordlist)
    print(f"{Fore.green}Wordlist saved successfully!{Style.reset}\n")
    print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")


def create_wordlist():
    wordlist_folder = select_difficulty()
    wordlist = edit_wordlist(None)
    save_new_wordlist(wordlist_folder, wordlist)
    print(f"\n{Fore.green}Wordlist saved successfully!{Style.reset}\n")
    print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")