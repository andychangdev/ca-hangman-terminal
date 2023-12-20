#!/bin/bash
if [[ -x "$(command -v python3)" ]] 
then
    python_version="$(python3 -V 2>&1)"
    if [[ $python_version != "Python 3"* ]] 
    then
        echo "Python 3.9.x or higher is recommended for running this program." >&2
    else
        echo "You have Python 3 installed. You are ready to install the Hangman application." >&2
    fi 
else
    echo "This program requires Python 3 to be installed.
    To install Python, go to https://www.python.org/downloads/" >&2
fi
