from models.User import User

class Customer(User):
    def __init__(self, name, userName, password ,address):
        super().__init__(name, userName, password)
        self.__cart = []
        self.__payout = 0 
        self.__address = address

    def getCart(self):
        return self.__cart
    
    def cartAdd(self, movieName):
        self.__cart.append(movieName)

    def increasePayment(self):
        self.__payout += 10

    def getPayout(self):
        return self.__payout
    
    def getAddress(self):
        return self.__address
    
