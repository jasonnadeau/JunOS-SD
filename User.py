__author__ = 'Jason Nadeau'

class JunosUser(object):
    def __init__(self, username, password):
        self.__setUsername(username)
        self.__setPassword(password)

    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password

    def __setUsername(self,username):
        self.__username=username

    def __setPassword(self,password):
        self.__password=password

    
