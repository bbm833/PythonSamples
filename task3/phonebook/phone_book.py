#!/usr/bin/env python3
from . phone_book_serializer import PhoneBookSerializer


class PhoneBook:
    def __init__(self, file_name):
        self.phone_book = {}
        self.serializer = PhoneBookSerializer(file_name)

    def add(self, name, phone_number):
        """Add new contact to phone book."""
        if name not in self.phone_book:
            self.phone_book[name] = phone_number
            return True

        return False

    def __check_name(function):
        def phone_book_operation(self, *args):
            name = args[0]
            if name in self.phone_book:
                return function(self, *args)
            else:
                return None
        return phone_book_operation

    @__check_name
    def update(self, name, phone_number):
        """Update an existing contact in the phone book."""
        self.phone_book[name] = phone_number
        return True

    @__check_name
    def delete(self, name):
        """Delete an existing contact."""
        del self.phone_book[name]
        return True

    @__check_name
    def find(self, name):
        """Return the phone number of a contact."""
        return self.phone_book[name]

    def find_all(self):
        return self.phone_book.items()

    def read_phone_book_file(self):
        """Load content of a phone book file."""
        is_file_read, self.phone_book = self.serializer.read()
        return is_file_read

    def write_phone_book_file(self):
        """Write content of the phone book in memory to of a phone book file."""
        is_file_updated = self.serializer.write(self.phone_book)
        return is_file_updated

