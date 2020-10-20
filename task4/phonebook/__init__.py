from configparser import ConfigParser
#from . phone_book_application import PhoneBookApplication

config = ConfigParser()
config.read('config.ini')
input_type = config.get('main', 'input_type').lower()
