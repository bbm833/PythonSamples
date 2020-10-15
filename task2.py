#!/usr/bin/env python3

class PhoneBook:
    def __init__(self):
        self.phone_book = {}

    #   def __function_generator__(self, function):
    #       def phone_book_operation(name, phone_number=None):
    #           if name in self.phone_book:
    #               function(name, phone_number)
    #               return True
    #           else:
    #               return False
    #       return phone_book_operation

    def add_contact(self, name, phone_number):
        if name not in self.phone_book:
            self.phone_book[name] = phone_number
            return True

        return False

    def find_contact(self, name):
        if name in self.phone_book:
            return self.phone_book[name]

        return ''

    def update_contact(self, name, phone_number):
        if name in self.phone_book:
            self.phone_book[name] = phone_number
            return True

        return False

    def delete_contact(self, name):
        if name in self.phone_book:
            del self.phone_book[name]
            return True

        return False

    def print(self):
        print("\n----------------------------------------------------------------------------")
        print("Name\t\t\t\tPhone Number")
        for name, phone_number in self.phone_book.items():
            print(f"{name}\t\t\t\t{phone_number}")
        print("----------------------------------------------------------------------------\n")


class PhoneBookApplication:

    def __init__(self):
        self.phone_book = PhoneBook()

    @staticmethod
    def print_menu():
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
        name = self.__get_name_from_console__()
        phone_number = self.__get_number_from_console__()

        is_added = self.phone_book.add_contact(name, phone_number)
        if is_added:
            print(f"Contact '{name}' is added to the phone book")
        else:
            is_confirmed = self.__is_operation_confirmed__(f"{name} is already in the phone book. "
                                                           "Do you want to update the number [Y/n]: ")
            if is_confirmed:
                self.update_contact(name, phone_number)

    def update_contact(self, name=None, phone_number=None):
        if name is None:
            name = self.__get_name_from_console__()

        if phone_number is None:
            phone_number = self.__get_number_from_console__()

        is_updated = self.phone_book.update_contact(name, phone_number)
        if is_updated:
            print(f"Phone number of '{name}' is updated as '{phone_number}'")
        else:
            print(f"'{name}' is not in the phone book.")

    def find_contact(self):
        name = self.__get_name_from_console__()
        phone_number = self.phone_book.find_contact(name)

        if phone_number:
            print(f"Phone number of '{name}' is '{phone_number}'.")
        else:
            print(f"'{name}' is not in phone book.")

    def delete_contact(self):
        name = self.__get_name_from_console__()
        is_confirmed = self.__is_operation_confirmed__(f"Do you want to delete contact '{name}' [Y/n]: ")

        if is_confirmed:
            is_deleted = self.phone_book.delete_contact(name)
            if is_deleted:
                print(f"Contact '{name}' is deleted.")
            else:
                print(f"'{name}' is not in the phone book.")

    def print_phone_book(self):
        self.phone_book.print()

    @staticmethod
    def __get_name_from_console__():
        return str(input("Enter the name of the contact: "))

    @staticmethod
    def __get_number_from_console__():
        return str(input("Enter the phone number of the contact: "))

    @staticmethod
    def __is_operation_confirmed__(message):
        while True:
            answer = str(input(message))
            if answer == "Y" or answer == "y":
                return True
            elif answer == "N" or answer == "n":
                return False
            else:
                print("Please enter a valid selection !!!")


if __name__ == "__main__":
    phone_book_application = PhoneBookApplication()
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
