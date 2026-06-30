from models.User import User

class Manager(User):
    def __init__(self, name, userName, password):
        super().__init__(name, userName, password)