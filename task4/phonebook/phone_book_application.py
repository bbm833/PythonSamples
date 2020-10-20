#!/usr/bin/env python3
from . phone_book import PhoneBook


class PhoneBookApplication:

    def __init__(self, phone_book_file_name):
        self.phone_book = PhoneBook(phone_book_file_name)
        is_file_read = self.phone_book.read_phone_book()
        if not is_file_read:
            print(f"{phone_book_file_name} is not a valid phone book file")

    def run(self):
        """In an infinite loop, get user selection and execute related function until 'Exit' is selected by the user"""
        while True:
            self.__print_menu()
            is_execution_ended = self.__execute_selection()
            if is_execution_ended:
                break
            input("Press Enter to continue...")

    def __execute_selection(self):
        """Get user selection and execute related function"""
        selection = input("Please make a selection [1-6] ")
        if selection == "1":
            self.__add_contact()
        elif selection == "2":
            self.__find_contact()
        elif selection == "3":
            self.__update_contact()
        elif selection == "4":
            self.__delete_contact()
        elif selection == "5":
            self.__print_phone_book()
        elif selection == "6":
            print("Bye !!!")
            return True
        else:
            print("Invalid selection. Please enter a number between 1 and 6")

        return False

    @staticmethod
    def __print_menu():
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

    def __add_contact(self):
        """Get the name and number of a contact and add it as new contact."""
        name = self.__get_name_from_console()
        phone_number = self.__get_number_from_console()

        is_contact_added = self.phone_book.add(name, phone_number)
        if is_contact_added:
            self.__write_phone_book_file()
            print(f"Contact '{name}' is added to the phone book")
        else:
            print(f"{name} is already in the phone book. ")

    def __update_contact(self):
        """Get the name and number of an existing contact and  update the number."""
        name = self.__get_name_from_console()
        phone_number = self.__get_number_from_console()

        is_updated = self.phone_book.update(name, phone_number)
        if is_updated:
            self.__write_phone_book_file()
            print(f"Phone number of '{name}' is updated as '{phone_number}'")
        else:
            print(f"'{name}' is not in the phone book.")

    def __find_contact(self):
        """Get the name of contact and add display the phone number."""
        name = self.__get_name_from_console()
        phone_number = self.phone_book.find(name)

        if phone_number:
            print(f"Phone number of '{name}' is '{phone_number}'.")
        else:
            print(f"'{name}' is not in phone book.")

    def __delete_contact(self):
        """Get the name of contact and delete it."""
        name = self.__get_name_from_console()
        is_confirmed = self.__is_operation_confirmed(f"Do you want to delete contact '{name}' [Y/n]: ")

        if is_confirmed:
            is_deleted = self.phone_book.delete(name)
            if is_deleted:
                self.__write_phone_book_file()
                print(f"Contact '{name}' is deleted.")
            else:
                print(f"'{name}' is not in the phone book.")

    def __print_phone_book(self):
        """Print phone book."""
        padding_size = 30
        print("\n----------------------------------------------------------------------------")
        print(f"{'Name':{padding_size}}Phone Number")
        for name, phone_number in self.phone_book.find_all():
            print(f"{name:{padding_size}}{phone_number}")
        print("----------------------------------------------------------------------------\n")

    def __write_phone_book_file(self):
        """Update phone book file."""
        is_file_written = self.phone_book.write_phone_book()
        if not is_file_written:
            print("Phone book file could not be updated")

    @staticmethod
    def __get_name_from_console():
        """Get contact name from the user."""
        return input("Enter the name of the contact: ")

    @staticmethod
    def __get_number_from_console():
        """Get phone number from the user."""
        return input("Enter the phone number of the contact: ")

    @staticmethod
    def __is_operation_confirmed(message):
        """Ask confirmation from the user."""
        while True:
            answer = input(message).upper()
            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                print("Please enter a valid selection !!!")

 
