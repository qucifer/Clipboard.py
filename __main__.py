# Importing modules #

import sys
import clipboard
import json

# Variable for data being saved to .JSON #

SAVED_DATA = "clipboard.json"

# Functions for writing and reading .JSON files #

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Ensure 2 cmd line Args #

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")

        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)

    else:
        print("Unknown Command")

else:
    print("Please pass exactly one command.")

