import inquirer
from wordlist_utilities import select_difficulty, prompt_user, edit_wordlist, save_new_wordlist

def create_wordlist():
    wordlist_name = prompt_user("Name of your wordlist")
    wordlist_folder = select_difficulty()
    wordlist = edit_wordlist(None)
    save_new_wordlist(wordlist_name, wordlist_folder, wordlist)