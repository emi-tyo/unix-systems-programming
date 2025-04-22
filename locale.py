#!/usr/bin/env python3

import sys
import os

def read_file(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        print("Error: File does not exist or is not readable.")
        sys.exit()
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file if line.strip()]

def list_locales(file_data):
    locales = [entry[2] for entry in file_data if entry[0] == 'locale']
    if locales:
        print("Available locales:")
        for locale in locales:
            print(locale)
    else:
        print("No locales available")

def list_charmaps(file_data):
    charmaps = [entry[2] for entry in file_data if entry[0] == 'charmap']
    if charmaps:
        print("Available charmaps:")
        for charmap in charmaps:
            print(charmap)
    else:
        print("No charmaps available")

def language_details(file_data, language):
    locales = sum(1 for entry in file_data if entry[0] == 'locale' and entry[1] == language)
    charmaps = sum(1 for entry in file_data if entry[0] == 'charmap' and entry[1] == language)
    if locales or charmaps:
        print("Language " + language + ":")
        print("Total number of locales: " + str(locales))
        print("Total number of charmaps: " + str(charmaps))
    else:
        print("No locales or charmaps in this " + language)


def print_version():
    print("Name: Emi")
    print("Surname: Sekikawa")
    print("Student ID: 14507608")
    print("Date of completion: 17/05/2024")

def main():
    if len(sys.argv) < 3:
        print("Incorrect syntax. Please check the command and try again.")
        sys.exit()

    option = sys.argv[1]
    argument_file = sys.argv[2]

    file_data = read_file(argument_file)

    if option == '-a':
        list_locales(file_data)
    elif option == '-m':
        list_charmaps(file_data)
    elif option == '-l' and len(sys.argv) == 4:
        language = sys.argv[3]
        language_details(file_data, language)
    elif option == '-v':
        print_version()
    else:
        print("Invalid option or incorrect syntax.")

if __name__ == "__main__":
    main()

