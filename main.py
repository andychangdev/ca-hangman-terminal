from play_hangman import play_hangman
from choose_wordlist import choose_wordlist

print("Welcome to Hangman!\n")

def display_menu():
    print("1. Play Hangman")
    print("2. Select Wordlist")
    print("3. Modify Wordlist")
    print("4. Create Wordlist")
    print("5. Exit")

display_menu()

while True:
    choice = input("\nEnter your selection (1-5): ")

    if choice == '1':
        play_hangman()
        display_menu()
    elif choice == '2':
        choose_wordlist()
        display_menu()
    elif choice == '3':
        print("\nModifying Wordlist...\n")
        display_menu()
    elif choice == '4':
        print("\nCreating Wordlist...\n")
        display_menu()
    elif choice == '5':
        print("\nOk, thanks for playing! See you next time!\n")
        break
    else:
        print("\nInvalid input. Please enter a valid option (1-5).")
