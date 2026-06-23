import customtkinter as ctk

from .CreateAccountWindow import CreateAccountWindow
from controllers.Application import Application
from .CustomerWindow import CustomerWindow

class LoginWindow(ctk.CTk):

    def __init__(self, customerArchive):
        super().__init__()
        self.customerArchive = customerArchive

        self.title("FlixNet")
        self.geometry("600x500")

        self.welcomeMessage = ctk.CTkLabel(self, text="Bem-vindo à FlixNet - FILMES HD", font=("PAPYRUS", 25))
        self.welcomeMessage.pack(pady=30)

        self.usernameMessage = ctk.CTkLabel(self, text="Nome de usuário:", font=("PAPYRUS", 20))
        self.usernameMessage.pack(pady=10)

        self.entryUsername = ctk.CTkEntry(self)
        self.entryUsername.pack(pady=10)

        self.passwordMessage = ctk.CTkLabel(self, text="Senha:", font=("PAPYRUS", 20))
        self.passwordMessage.pack(pady=10)

        self.entryPassword = ctk.CTkEntry(self, show="\u2022")
        self.entryPassword.pack(pady=10)

        self.loginButton = ctk.CTkButton(self, text="Entrar", font=("PAPYRUS", 20, "bold"), command=self.login)
        self.loginButton.pack(pady=10)

        self.createAccountButton = ctk.CTkButton(self, text="Criar usuário", font=("PAPYRUS", 20, "bold"), command=self.openCreateAccount)
        self.createAccountButton.pack(pady=10)

    def openCreateAccount(self):
        self.withdraw()
        CreateAccountWindow(self, self.customerArchive)

    def login(self):
        customer = Application.validateLogin(self.customerArchive, self.entryUsername.get(), self.entryPassword.get())
        if (customer):
            self.withdraw()
            CustomerWindow(self, customer)
        else:
            self.errorLabel = ctk.CTkLabel(self, text="Usuário ou senha inválidos")
            self.errorLabel.pack()