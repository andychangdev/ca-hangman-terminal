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

def choose_wordlist():
    selected_difficulty = select_difficulty()
    print(selected_difficulty)
    print(type(selected_difficulty))

choose_wordlist()


