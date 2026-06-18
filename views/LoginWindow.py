import customtkinter as ctk

from CreateAccountWindow import CreateAccountWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

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

        self.loginButton = ctk.CTkButton(self, text="Entrar", font=("PAPYRUS", 20, "bold"))
        self.loginButton.pack(pady=10)

        self.createAccountButton = ctk.CTkButton(self, text="Criar usuário", font=("PAPYRUS", 20, "bold"), command=self.openCreateAccount)
        self.createAccountButton.pack(pady=10)

    def openCreateAccount(self):
        self.withdraw()
        CreateAccountWindow(self)


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()