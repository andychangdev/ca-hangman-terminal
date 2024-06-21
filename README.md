<img src="./docs/banner.jpg" alt="banner"></img>

<h1 align="center">Documentation for Hangman CLI Terminal Application</h1>

<p align="center">
  <a href="#💡-purpose">Purpose</a> •
  <a href="#⚙️-functionality">Functionality</a> •
  <a href="#📀-installation-guide">Installation Guide</a> •
  <a href="#📝-development-logs">Development Logs</a> •
  <a href="#📚-references">References</a>
</p>

## 💡 Purpose

- This terminal application showcases my ability to utilise a range of programming concepts and structures using Python. It includes 4 features that demonstrate my understanding of variables, scope, loops, conditional control structures and error handling.

## ⚙️ Functionality

1. **Play Hangman**
    
    This feature allows the user to play Hangman. The game will generate a random hidden word for the user to guess. The user has a total of 7 lives to guess the hidden word.

2. **Select Wordlist**

    This feature allows the user to select a word list of their choice. Wordlists are categorised by difficulty: easy, medium, and hard.

3. **Modify Wordlist**

    This feature allows the user to modify wordlists. The user can select which word list to modify and then add or remove words from the selected word list. After modifying the word list, it will be saved for future use.

4.  **Create Wordlist**

    This feature allows the user to create their own wordlist. The user can add new or remove words to or from the wordlist. After creating their word list, they can name it and save it for future use.

## 📀 Installation Guide

### System Requirements
- **Operating System:**

    MacOS 10.13 or later

- **Python Version:**
    
    Python 3.9.x or higher is recommended for running this application.

### Installation Steps

1. **Download the Git Repository**

    Download the Git repository by clicking on the green "< > code" button, then click "Download ZIP". 
    
    You can also run the following command in your preferred terminal application to clone the repository:
    ```bash
    git clone https://github.com/andychangdev/ca-hangman-terminal.git
    ```

2. **Navigate to the Application Directory**

     Using your file explorer (Finder or Explorer), locate the folder where you downloaded or cloned the repository.

    You can also run the following command after cloning the repository to change the working directory to the application directory:
    ```bash
    cd ca-hangman-terminal
    ```
3. **Ensure Python 3 is installed**

    Before installing the application, ensure that Python 3 is installed on your computer. If Python 3 is not installed, you can download it from the official Python website and follow the installation instructions specific to your operating system. 

    You can double-click on the `check_python.sh` script within the application folder to check if you have Python 3 installed. You can also run the following command to check if Python 3 is installed:

    ```bash
    bash check_python.sh
    ```

3. **Run the Installation Script**

    After checking Python 3 is installed, double-click on the `install.sh` script within the application folder. This action will initiate the setup process for the Hangman game.

    You can also run the following command to execute the installation script:

    ```bash
    bash install.sh
    ```

4. **Play the Game**

    Once the installation is complete, double-click on the `hangman.sh` to run the game.

    You can also run the following command to run the game:

    ```bash
    bash hangman.sh
    ```

## 📝 Development Logs

### Implementation Plan

![screenshot](./docs/trello_screenshots/trello_userboard1.jpg)
![screenshot](./docs/trello_screenshots/trello_userboard2.jpg)
![screenshot](./docs/trello_screenshots/trello_userboard3.jpg)
![screenshot](./docs/trello_screenshots/trello_userboard4.jpg)
![screenshot](./docs/trello_screenshots/trello_userboard5.jpg)
![screenshot](./docs/trello_screenshots/trello_userboard6.jpg)
![screenshot](./docs/trello_screenshots/trello_main_menu.jpg)
![screenshot](./docs/trello_screenshots/trello_play_hangman.jpg)
![screenshot](./docs/trello_screenshots/trello_multiple_wordlist.jpg)
![screenshot](./docs/trello_screenshots/trello_modify_wordlist.jpg)
![screenshot](./docs/trello_screenshots/trello_create_wordlist.jpg)
![screenshot](./docs/trello_screenshots/trello_run_application.jpg)
![screenshot](./docs/trello_screenshots/trello_documentation.jpg)
![screenshot](./docs/trello_screenshots/trello_git.jpg)



### Manual Testing
![screenshot](./docs/manual_testing/19_12_23_manual_test.png)
![screenshot](./docs/manual_testing/20-12-23_manual_test.png)

## 📚 References

### Code Style Guide

This terminal application adheres to the Python Enhancement Proposal 8 (PEP 8) coding style guide, established by Guido van Rossum, Barry Warsaw, and Nick Coghlan.

### App Dependencies

```
blessed==1.20.0
colored==2.2.3
inquirer==3.1.4
pyfiglet==1.0.2
python-editor==1.0.4
readchar==4.0.5
six==1.16.0
wcwidth==0.2.12
```

### Third Party Packages
This terminal application uses the following third-party resources:

- [Inquirer](https://pypi.org/project/inquirer/)
- [Colored](https://pypi.org/project/colored/)
- [Pyfiglet](https://pypi.org/project/pyfiglet/)

### Third Party Resources

1. Nate Babaev 2022, 5 Python Libraries for Building Command Line Tools, online video, viewed 17 December 2023, https://www.youtube.com/watch?v=20Qkq93kwKw

2. Rossum, G 2001, 'PEP 8 - Style Guide for Python Code', Python Enhancement Proposal, 05 July, viewed 16 December, https://peps.python.org/pep-0008/

