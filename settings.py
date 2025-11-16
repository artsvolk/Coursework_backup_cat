import configparser

def get_token():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config['tokens']['ya_disk']