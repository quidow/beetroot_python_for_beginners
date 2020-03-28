"""
Extend Phonebook application

Functionality of Phonebook application:

- Add new entries 
- Search by first name 
- Search by last name 
- Search by full name
- Search by telephone number
- Search by city or state
- Delete a record for a given telephone number
- Update a record for a given telephone number
- An option to exit the program

The first argument to the application should be the name of the phonebook. 
Application should load JSON data, if it is present in the folder with 
application, else raise an error. After the user exits, all data should be 
saved to loaded JSON.
"""

import sys
import argparse
import json

parser = argparse.ArgumentParser(description='Extend Phonebook application')
parser.add_argument('-f', default="phonebook.json", help="""Path to JSON file 
                    to store phonebook entries""")
args = parser.parse_args()

def save_phonebook(phonebook_file=args.f):
    with open(phonebook_file, "w") as f:
        json.dump(phonebook, f)
        f.close()

def search_entry(key, value):
    for entry in phonebook:
        if value == entry[key]:
            return entry
    else:
        return False

def search_entries(key, value):
    entries = []
    for entry in phonebook:
        if value == entry[key]:
            entries.append(entry)
    return entries

def add_or_edit_entry(entry=None):
    entry = entry or {}        
    entry["first_name"] = input("Enter first name: ")
    entry["last_name"] = input("Enter last name: ")
    entry["full_name"] = entry["first_name"] + " " + entry["last_name"]
    entry["telephone"] = input("Enter telephone: ")
    entry["state"] = input("Enter state: ")
    entry["city"] = input("Enter city: ")
    return entry

def print_entry(entry):
    for key, elem in entry.items():
        print("{0:10} {1}".format(key, elem))

with open(args.f, "r") as f:
    phonebook = json.load(f)
    f.close()

while True:
    print("Choose your option:", "1) Add", "2) Search", "3) Update",
          "4) Delete", "5) Quit", sep="\n")
    x = input()
    if x == "1":
        phonebook.append(add_or_edit_entry())
        save_phonebook()
    elif x == "2":
        print("Search by:", "1) First name", "2) Last name", "3) Full name",
              "4) Telephone number", "5) City", "6) State", sep="\n")
        x = input()
        if x == "1":
            entries = search_entries("first_name", input("Enter first name:"))
        elif x == "2":
            entries = search_entries("last_name", input("Enter last name:"))
        elif x == "3":
            entries = search_entries("full_name", input("Enter full name:"))
        elif x == "4":
            entries = search_entries("telephone", input("Enter telephone number:"))
        elif x == "5":
            entries = search_entries("city", input("Enter city:"))
        elif x == "6":
            entries = search_entries("state", input("Enter state:"))
        if entries:
            for entry in entries:
                print_entry(entry)
        else:
            print("No entry found")
            continue
    elif x == "3":
        entry = search_entry("telephone", input("Enter telephone: "))
        if entry:
            print_entry(entry)
            add_or_edit_entry(entry)
            save_phonebook()
        else:
            print("No entry found")
            continue
    elif x == "4":
        entry = search_entry("telephone", input("Enter telephone: "))
        if entry:
            print_entry(entry)
            del phonebook[phonebook.index(entry)]
            save_phonebook()
        else:
            print("No entry found")
            continue
    elif x in ("5", "q", "Q"):
        exit()
