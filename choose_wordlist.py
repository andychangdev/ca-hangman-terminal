import os


def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        selection = input("Enter your selection (1-3): ")
        try:
            if selection in ["1", "2", "3"]:
                return selection
            else:
                print("Invalid input. Please enter a valid number (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def select_wordlist(difficulty):
    difficulty_folders = {
        '1': 'easy',
        '2': 'medium',
        '3': 'hard'
    }
    selected_difficulty = difficulty_folders.get(difficulty)

    if selected_difficulty:
        folder_path = os.path.join('wordlists', selected_difficulty)
        wordlists = os.listdir(folder_path)

        print(f"Select from available {selected_difficulty} wordlists:")
        for index, wordlist in enumerate(wordlists, start=1):
            print(f"{index}. {wordlist}")
        while True:
            selection = input(f"Enter the number corresponding to your preferred wordlist: ")
            try:
                selection = int(selection)
                if 1 <= selection <= len(wordlists):
                    selected_wordlist = wordlists[selection - 1]
                    wordlist_filepath = os.path.join(folder_path, selected_wordlist)
                    return wordlist_filepath
                else:
                    print("Invalid input. Please select a valid wordlist number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        

def choose_wordlist():
    selected_difficulty = select_difficulty()
    selected_wordlist_filepath = select_wordlist(selected_difficulty)
    with open("active_wordlist.txt", 'w') as file:
        file.write(selected_wordlist_filepath)
    print(f"Wordlist saved")


