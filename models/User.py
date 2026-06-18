class User:
    def __init__(self, name, userName, password):
        self.__name = name
        self.__userName = userName
        self.__password = password

    def getName(self):
        return self.__name
    
    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return self.__password
    
    