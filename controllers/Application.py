import string
from models.CustomerArchive import CustomerArchive
from controllers.Hash import Hash

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
        if not any(char.islower() for char in password):
            return False
        return True
    
    @staticmethod
    def validateLogin(conn, username: str, password: str):
        row = conn.execute(
            "SELECT * FROM customer WHERE username = ?", (username,)
        ).fetchone()

        if row and Hash.check_password(password, row["password"]):
            return row  # retorna os dados do cliente logado
        return None
