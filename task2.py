#!/usr/bin/env python3

import pickle


class PhoneBook:
    def __init__(self, phone_book_file_name):
        self.phone_book = {}
        self.phone_book_file_name = phone_book_file_name

    def add_contact(self, name, phone_number):
        """Add new contact to phone book."""
        if name not in self.phone_book:
            self.phone_book[name] = phone_number
            return True

        return False

    def __function_generator(function):
        def phone_book_operation(self, *args):
            name = args[0]
            if name in self.phone_book:
                return function(self, *args)
            else:
                return None
        return phone_book_operation

    @__function_generator
    def update_contact(self, name, phone_number):
        """Update an existing contact in the phone book."""
        self.phone_book[name] = phone_number
        return True

    @__function_generator
    def delete_contact(self, name):
        """Delete an existing contact."""
        del self.phone_book[name]
        return True

    @__function_generator
    def find_contact(self, name):
        """Return the phone number of a contact."""
        return self.phone_book[name]

    def print(self):
        """Print the content of the phone book."""
        print("\n----------------------------------------------------------------------------")
        print("Name\t\t\t\tPhone Number")
        for name, phone_number in self.phone_book.items():
            print(f"{name}\t\t\t\t{phone_number}")
        print("----------------------------------------------------------------------------\n")

    def read_phone_book_file(self):
        """Load content of a phone book file."""
        is_file_read = True
        try:
            with open(self.phone_book_file_name, 'rb') as phone_book_file:
                self.phone_book = pickle.load(phone_book_file)
        except (IOError, OSError, pickle.PickleError, pickle.UnpicklingError):
            is_file_read = False
        return is_file_read

    def write_phone_book_file(self):
        """Write content of the phone book in memory to of a phone book file."""
        is_file_written = True
        try:
            with open(self.phone_book_file_name, 'wb') as phone_book_file:
                pickle.dump(self.phone_book, phone_book_file)
        except (IOError, OSError, pickle.PickleError, pickle.UnpicklingError):
            is_file_written = False
        return is_file_written


class PhoneBookApplication:

    def __init__(self, phone_book_file_name):
        self.phone_book = PhoneBook(phone_book_file_name)
        is_file_read = self.phone_book .read_phone_book_file()
        if not is_file_read:
            print(f"{phone_book_file_name} is not a valid phone book file")

    @staticmethod
    def print_menu():
        """Print menu."""
        print("""
############################################################################
#                                                                          #
#                   Welcome to Phone Book Application                      #
#                                                                          #
# 1. Add a new contact                                                     #
# 2. Find phone number                                                     #
# 3. Update a phone number                                                 #
# 4. Delete a contact                                                      #
# 5. Print phone book                                                      #
# 6. Exit                                                                  #
#                                                                          #
############################################################################""")

    def add_contact(self):
        """Get the name and number of a contact and add it as new contact."""
        name = self.__get_name_from_console()
        phone_number = self.__get_number_from_console()

        is_contact_added = self.phone_book.add_contact(name, phone_number)
        if is_contact_added:
            print(f"Contact '{name}' is added to the phone book")
        else:
            is_confirmed = self.__is_operation_confirmed(f"{name} is already in the phone book. "
                                                           "Do you want to update the number [Y/n]: ")
            if is_confirmed:
                self.update_contact(name, phone_number)
                is_contact_added = True

        if is_contact_added:
            self.__write_phone_book_file()

    def update_contact(self, name=None, phone_number=None):
        """Get the name and number of an existing contact and  update the number."""
        if name is None:
            name = self.__get_name_from_console()

        if phone_number is None:
            phone_number = self.__get_number_from_console()

        is_updated = self.phone_book.update_contact(name, phone_number)
        if is_updated:
            self.__write_phone_book_file()
            print(f"Phone number of '{name}' is updated as '{phone_number}'")
        else:
            print(f"'{name}' is not in the phone book.")

    def find_contact(self):
        """Get the name of contact and add display the phone number."""
        name = self.__get_name_from_console()
        phone_number = self.phone_book.find_contact(name)

        if phone_number:
            print(f"Phone number of '{name}' is '{phone_number}'.")
        else:
            print(f"'{name}' is not in phone book.")

    def delete_contact(self):
        """Get the name of contact and delete it."""
        name = self.__get_name_from_console()
        is_confirmed = self.__is_operation_confirmed(f"Do you want to delete contact '{name}' [Y/n]: ")

        if is_confirmed:
            is_deleted = self.phone_book.delete_contact(name)
            if is_deleted:
                self.__write_phone_book_file()
                print(f"Contact '{name}' is deleted.")
            else:
                print(f"'{name}' is not in the phone book.")

    def print_phone_book(self):
        """Print phone book."""
        self.phone_book.print()

    def __write_phone_book_file(self):
        """Update phone book file."""
        is_file_written = self.phone_book.write_phone_book_file()
        if not is_file_written:
            print("Phone book file could not be updated")

    @staticmethod
    def __get_name_from_console():
        """Get contact name from the user."""
        return str(input("Enter the name of the contact: "))

    @staticmethod
    def __get_number_from_console():
        """Get phone number from the user."""
        return str(input("Enter the phone number of the contact: "))

    @staticmethod
    def __is_operation_confirmed(message):
        """Ask confirmation from the user."""
        while True:
            answer = str(input(message))
            if answer == "Y" or answer == "y":
                return True
            elif answer == "N" or answer == "n":
                return False
            else:
                print("Please enter a valid selection !!!")


if __name__ == "__main__":
    phone_book_application = PhoneBookApplication("MyPhoneBook.pb")
    while True:
        phone_book_application.print_menu()
        selection = str(input("Please make a selection [1-6] "))

        if selection == "1":
            phone_book_application.add_contact()
        elif selection == "2":
            phone_book_application.find_contact()
        elif selection == "3":
            phone_book_application.update_contact()
        elif selection == "4":
            phone_book_application.delete_contact()
        elif selection == "5":
            phone_book_application.print_phone_book()
        elif selection == "6":
            print("Bye !!!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 6")

        input("Press Enter to continue...")
