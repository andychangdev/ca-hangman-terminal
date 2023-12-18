from wordlist_utilities import select_difficulty, edit_wordlist, save_new_wordlist

def create_wordlist():
    while True:
        try:
            wordlist_name = input("Enter the name for your wordlist: ")
            if " " in wordlist_name:
                raise ValueError("Invalid input. Name must not contain spaces.")
            elif not wordlist_name.isalpha():
                raise ValueError("Invalid input. Name must only alphabet letters")
            elif len(wordlist_name) < 4:
                raise ValueError("Invalid input. Name must contain atleast 4 letters")
            else:
                break
        except ValueError as error:
            print(error)
    wordlist_folder = select_difficulty()
    wordlist = edit_wordlist(None)
    save_new_wordlist(wordlist_name, wordlist_folder, wordlist)
