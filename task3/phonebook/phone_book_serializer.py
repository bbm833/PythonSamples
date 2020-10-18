#!/usr/bin/env python3
from phonebook import config_type

if config_type == 'json':
    import json as serializer
    SerializerError = serializer.decoder.JSONDecodeError
    file_type = 't'
else:
    import pickle as serializer
    SerializerError = serializer.PickleError
    file_type = 'b'


class PhoneBookSerializer:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        """Load content of a phone book file."""
        phone_book = {}
        try:
            with open(self.file_name, f'r{file_type}') as file:
                phone_book = serializer.load(file)
        except (FileNotFoundError, IOError, OSError, SerializerError):
            return False, phone_book

        return True, phone_book

    def write(self, phone_book):
        """Write content of the phone book in memory to of a phone book file."""
        try:
            with open(self.file_name, f'w{file_type}') as file:
                serializer.dump(phone_book, file)
        except (IOError, OSError):
            return False
        return True
