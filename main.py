import customtkinter as ctk
from views.LoginWindow import LoginWindow
from models.CustomerArchive import CustomerArchive

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    customerArchive = CustomerArchive()
    app = LoginWindow(customerArchive)
    app.mainloop()