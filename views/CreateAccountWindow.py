import customtkinter as ctk
from controllers.Application import Application
from models.CustomerArchive import CustomerArchive
from CTkMessagebox import CTkMessagebox
from models.Customer import Customer

class CreateAccountWindow(ctk.CTkToplevel):

    def __init__(self, parent, customerArchive):
        super().__init__(parent)
        self.customerArchive = customerArchive

        self.title("Criação de conta")
        self.geometry("800x650")

        self.welcomeMessage = ctk.CTkLabel(self, text="Preencha o formulário abaixo", font=("PAPYRUS", 25))
        self.welcomeMessage.pack(pady=10)

        self.nameMessage = ctk.CTkLabel(self, text="Nome:", font=("PAPYRUS", 20))
        self.nameMessage.pack(pady=10)

        self.nameEntry = ctk.CTkEntry(self)
        self.nameEntry.pack(pady=10)

        self.usernameMessage = ctk.CTkLabel(self, text="Nome de usuário:", font=("PAPYRUS", 20))
        self.usernameMessage.pack(pady=10)

        self.usernameEntry = ctk.CTkEntry(self)
        self.usernameEntry.pack(pady=10)

        self.passwordMessage = ctk.CTkLabel(self, text="Senha:", font=("PAPYRUS", 20))
        self.passwordMessage.pack(pady=10)

        self.passwordEntry = ctk.CTkEntry(self, show="\u2022")
        self.passwordEntry.pack(pady=10)

        self.confirmPasswordMessage = ctk.CTkLabel(self, text="Confirme a senha:", font=("PAPYRUS", 20))
        self.confirmPasswordMessage.pack(pady=10)

        self.confirmPasswordEntry = ctk.CTkEntry(self, show="\u2022")
        self.confirmPasswordEntry.pack(pady=10)

        self.addressMessage = ctk.CTkLabel(self, text="Endereço:", font=("PAPYRUS", 20))
        self.addressMessage.pack(pady=10)

        self.addressEntry = ctk.CTkEntry(self)
        self.addressEntry.pack(pady=10)

        self.confirmButton = ctk.CTkButton(self, text="Confirmar", command=self.equalPasswords)
        self.confirmButton.pack(pady=10)

    def equalPasswords(self):
        self.invalidPasswordMessage = ctk.CTkLabel(self, text="")
        password = self.passwordEntry.get()
        confirmPassword = self.confirmPasswordEntry.get()

        if (password == confirmPassword) and (Application.PasswordVerify(password, confirmPassword)):
            self.customerArchive.add(Customer(self.nameEntry.get(), self.usernameEntry.get(), self.passwordEntry.get(), self.addressEntry.get()))   
            msg = CTkMessagebox(title="Sucesso", message="Usuário registrado com sucesso!")
            msg.wait_window() 
            self.master.deiconify()
            self.destroy()
        else:
            self.invalidPasswordMessage = ctk.CTkLabel(self, text="Senha inválida")
            self.invalidPasswordMessage.pack(pady=10)