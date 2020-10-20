from configparser import ConfigParser
#from . phone_book_application import PhoneBookApplication

config = ConfigParser()
config.read('config.ini')
config_type = config.get('main', 'config_type').lower()
