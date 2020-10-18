#!/usr/bin/env python3
from phonebook.phone_book_application import PhoneBookApplication
import argparse
__author__ = 'sdemiray'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PhoneBook v3 by sdemiray.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    args = parser.parse_args()

    phone_book_application = PhoneBookApplication(args.input)
    phone_book_application.run()
 
