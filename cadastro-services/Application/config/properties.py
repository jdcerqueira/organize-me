from configparser import ConfigParser
import os

class Properties():
    def __init__(self, section):
        self.properties = {}

        config = ConfigParser()
        config.read(os.path.abspath("config/config.properties"))
        for item in config[section]:
            self.properties[item] = config[section][item]