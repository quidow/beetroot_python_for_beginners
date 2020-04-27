import json
import os


def load_phonebook(phonebook_file=None):
    if phonebook_file and os.path.isfile(phonebook_file):
        with open(phonebook_file, "r") as f:
            return json.load(f)
    else:
        return []


def save_phonebook(phonebook_file, phonebook_object):
    with open(phonebook_file, "w") as f:
        json.dump(phonebook_object, f)


def search_entries(phonebook_object, key, value):
    entry_indexes = []
    for entry in phonebook_object:
        if value == entry.get(key, None):
            entry_indexes.append(phonebook_object.index(entry))
    return entry_indexes


def add_or_edit_entry(phonebook_object, entry_index=None):
    entry = phonebook_object[phonebook_object[entry_index]].copy() if entry_index else {}
    entry["first_name"] = input("Enter first name: ")
    entry["last_name"] = input("Enter last name: ")
    entry["full_name"] = entry["first_name"] + " " + entry["last_name"]
    entry["telephone"] = input("Enter telephone: ")
    entry["state"] = input("Enter state: ")
    entry["city"] = input("Enter city: ")
    return entry


def print_entries(phonebook_object, entry_indexes):
    if not entry_indexes:
        print("No entry found")
    for entry in entry_indexes:
        for key, elem in phonebook_object[entry].items():
            print("{0:10} {1}".format(key, elem))


