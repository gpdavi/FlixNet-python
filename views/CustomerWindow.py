import customtkinter as ctk
from controllers.Application import Application
from models.CustomerArchive import CustomerArchive
from CTkMessagebox import CTkMessagebox
from models.Customer import Customer


class CustomerWindow(ctk.CTkToplevel):
    def __init__(self, parent, customer):
        super().__init__(parent)

        self.title("Área do cliente")
        self.geometry("800x600")

        self.welcomeMessage = ctk.CTkLabel(self, text=f"Seja bem-vindo, {customer.getName()}")
        self.welcomeMessage.pack(pady=10)