import configparser

config = configparser.RawConfigParser()
config.read("config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationUrl(self):
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getApplicationUsername(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationPassord(self):
        passord = config.get('common info', 'passord')
        return passord
