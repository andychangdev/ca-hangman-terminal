from colored import Fore, Style
from game_components.wordlist_utilities import select_difficulty, select_wordlist, edit_wordlist, save_new_wordlist, save_wordlist


def choose_wordlist():
    try:
        selected_difficulty = select_difficulty()
        selected_wordlist_filepath = select_wordlist(selected_difficulty)
        active_wordlist_filepath = "wordlists/active_wordlist.txt"
        with open(active_wordlist_filepath, 'w') as file:
            file.write(selected_wordlist_filepath)
        print(f"{Fore.green}Wordlist selected!{Style.reset}\n")
    except Exception as error:
        print(f"{Fore.red}An unexpected error occurred: {error}{Style.reset}\n")
        return
    finally:
        print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")


def modify_wordlist():
    try:
        selected_difficulty = select_difficulty()
        wordlist_filepath = select_wordlist(selected_difficulty)
        wordlist = edit_wordlist(wordlist_filepath)
        if wordlist == "Exit":
            return
        else:
            save_wordlist(wordlist_filepath, wordlist)
            print(f"{Fore.green}Wordlist saved successfully!{Style.reset}\n")
    except Exception as error:
        print(f"{Fore.red}An unexpected error occurred: {error}{Style.reset}\n")
        return
    finally:
        print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")


def create_wordlist():
    try:
        wordlist_folder = select_difficulty()
        wordlist = edit_wordlist(None)
        if wordlist == "Exit":
            return
        else:
            save_new_wordlist(wordlist_folder, wordlist)
            print(f"\n{Fore.green}Wordlist saved successfully!{Style.reset}\n")
    except Exception as error:
        print(f"{Fore.red}An unexpected error occurred: {error}{Style.reset}\n")
        return
    finally:
        print(f"{Fore.cyan}Back to Main Menu...{Style.reset}\n")