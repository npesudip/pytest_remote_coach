import os
from pathlib import Path
import configparser

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.RawConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_email():
        username = config.get('common info', 'email')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
