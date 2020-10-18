from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
config_type = config.get('main', 'config_type').lower()
print(config_type)
