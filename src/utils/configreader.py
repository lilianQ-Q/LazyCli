import ConfigParser

class ConfigReader:
    def __init__(self, configFilePath):
        self.configparser = ConfigParser.ConfigParser()
        self.configFilePath = configFilePath
        self.configFile = self.configparser.read(self.configFilePath)
