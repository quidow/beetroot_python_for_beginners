import argparse
import phonebook

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extend Phonebook application')
    parser.add_argument('-f', default="phonebook.json", help="Path to JSON file to store phonebook entries")
    args = parser.parse_args()

    phonebook_object = phonebook.load_phonebook(args.f)

    while True:
        print("Choose your option:", "1) Add", "2) Search", "3) Update",
              "4) Delete", "5) Quit", sep="\n")
        x = input()
        if x == "1":
            phonebook_object.append(phonebook.add_or_edit_entry(phonebook_object))
            phonebook.save_phonebook(args.f, phonebook_object)
        elif x == "2":
            print("Search by:", "1) First name", "2) Last name", "3) Full name",
                  "4) Telephone number", "5) City", "6) State", sep="\n")
            x = input()
            entry_indexes = []
            if x == "1":
                entry_indexes = phonebook.search_entries(phonebook_object, "first_name", input("Enter first name:"))
            elif x == "2":
                entry_indexes = phonebook.search_entries(phonebook_object, "last_name", input("Enter last name:"))
            elif x == "3":
                entry_indexes = phonebook.search_entries(phonebook_object, "full_name", input("Enter full name:"))
            elif x == "4":
                entry_indexes = phonebook.search_entries(phonebook_object, "telephone", input("Enter telephone number:"))
            elif x == "5":
                entry_indexes = phonebook.search_entries(phonebook_object, "city", input("Enter city:"))
            elif x == "6":
                entry_indexes = phonebook.search_entries(phonebook_object, "state", input("Enter state:"))
            phonebook.print_entries(phonebook_object, entry_indexes)
        elif x == "3":
            entry_indexes = phonebook.search_entries(phonebook_object, "telephone", input("Enter telephone: "))
            if entry_indexes:
                phonebook.print_entries(phonebook_object, entry_indexes)
                phonebook_object[entry_indexes[0]] = phonebook.add_or_edit_entry(entry_indexes[0])
                phonebook.save_phonebook(args.f, phonebook_object)
            else:
                print("No entry found")
                continue
        elif x == "4":
            entry_indexes = phonebook.search_entries(phonebook_object, "telephone", input("Enter telephone: "))
            if entry_indexes:
                phonebook.print_entries(phonebook_object, entry_indexes[:1])
                del phonebook_object[entry_indexes[0]]
                phonebook.save_phonebook(args.f, phonebook_object)
            else:
                print("No entry found")
                continue
        elif x in ("5", "q", "Q"):
            exit()
