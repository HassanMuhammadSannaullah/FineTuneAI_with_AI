import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the .ini file
config.read('config.ini')

# Get the values from the [API] section
url = config.get('API', 'URL')
bearer = config.get('API', 'BEARER')
