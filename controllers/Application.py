import string
from models.CustomerArchive import CustomerArchive

class Application:
    def PasswordVerify(self,password):
        if len(password)<8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True
    
    def validateLogin(customerArchive, username, password):
        for customer in customerArchive.getCustomers():
            if (username == customer.getUserName() and password == customer.getPassword()):
                return customer
        return None