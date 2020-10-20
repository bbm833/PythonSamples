#!/usr/bin/env python3
from . phone_book_serializer import PhoneBookSerializer
from collections.abc import Collection


class PhoneBook(Collection):
    def __init__(self, file_name):
        self.phone_book = {}
        self.serializer = PhoneBookSerializer(file_name)

    def add(self, name, phone_number):
        """Add new contact to phone book."""
        if name not in self.phone_book:
            self.phone_book[name] = phone_number
            return True

        return False

    def __contact_exists(function):
        def phone_book_operation(self, *args):
            name = args[0]
            if self.contains(name):
                return function(self, *args)
            else:
                return None
        return phone_book_operation

    @__contact_exists
    def update(self, name, phone_number):
        """Update an existing contact in the phone book."""
        self.phone_book[name] = phone_number
        return True

    @__contact_exists
    def delete(self, name):
        """Delete an existing contact."""
        del self.phone_book[name]
        return True

    @__contact_exists
    def find(self, name):
        """Return the phone number of a contact."""
        return self.phone_book[name]

    def __contains__(self, name):
        return name in self.phone_book

    def __iter__(self):
        return iter(phone_book)

    def __next__(self):
        return next(phone_book)

    def __len__(self):
        return len(phone_book)

    def __setitem__(self, name, phone_number):
        self.phone_book[name] = phone_number

    def find_all(self):
        return self.phone_book.items()

    def read_phone_book(self):
        """Load content of a phone book file."""
        is_file_read, self.phone_book = self.serializer.read()
        return is_file_read

    def write_phone_book(self):
        """Write content of the phone book in memory to of a phone book file."""
        is_file_updated = self.serializer.write(self.phone_book)
        return is_file_updated

