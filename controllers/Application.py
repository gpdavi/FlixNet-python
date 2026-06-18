import string
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
    
    def confirmPassword(self,password,confirmation):
        if password != confirmation:
            return False
        return True