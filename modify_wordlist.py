from wordlist_utilities import select_difficulty, select_wordlist, edit_wordlist, save_wordlist


def modify_wordlist():
    selected_difficulty = select_difficulty()
    wordlist_filepath = select_wordlist(selected_difficulty)
    wordlist = edit_wordlist(wordlist_filepath)
    save_wordlist(wordlist_filepath, wordlist)