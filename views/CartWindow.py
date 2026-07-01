import customtkinter as ctk
from controllers.Application import Application
from models.CustomerArchive import CustomerArchive
from CTkMessagebox import CTkMessagebox
from models.Customer import Customer
from PIL import Image
import requests
from io import BytesIO
from functools import partial
from views.MovieWindow import MovieWindow

class CartWindow(ctk.CTkToplevel):
    def __init__(self, parent, customer):
        
        super().__init__(parent)
        self.customer = customer
        self.parent = parent
        self.state("zoomed")
        cart  = self.customer.getCart()

        self.title("Carrinho de compras")
        ctk.CTkLabel(self, text=f"Seja bem-vindo ao carrinho de compras, {self.customer.getName().capitalize()}",  font=("Arial", 22)).pack(pady=10)
        
        cartFrame = ctk.CTkFrame(self, height=800, width=800)
        

        for movieName in cart:
            ctk.CTkLabel(cartFrame, text=f"{movieName}................ R$ 10,00", font=("Papyrus", 20)).pack(pady=3)
        
        ctk.CTkLabel(cartFrame, text=f"Endereço de entrega: {self.customer.getAddress()}").pack()

        ctk.CTkLabel(cartFrame, text=f"Total a pagar: R$ {self.customer.getPayout()}", font=("Arial", 22)).pack(pady=3)
        ctk.CTkButton(cartFrame, text="Finalizar compra", font=("Arial", 22), command=self.finishPurchase).pack(pady=3)

        cartFrame.pack()

    def finishPurchase(self):
        conn = CustomerArchive.connection()
        conn_rented = CustomerArchive.connection_rented()
        try:
            customer_id = CustomerArchive.get_id_by_username(conn, self.customer.getUserName())
            if customer_id is None:
                CTkMessagebox(title="Erro", message="Cliente não encontrado no banco de dados.")
                return

            CustomerArchive.table_rented(conn_rented)  # garante que a tabela existe

            cart = self.customer.getCart()
            for movieName in cart:
                CustomerArchive.insert_rented(conn_rented, customer_id, movieName)
        finally:
            conn.close()
            conn_rented.close()

        CTkMessagebox(title="Compra finalizada", message=f"Compra finalizada! \nTotal a pagar: R$ {self.customer.getPayout():.2f}")
        self.customer.clearCart()
        self.after(50, self.closeAndReturn)


    def closeAndReturn(self):
        self.parent.state("zoomed")
        self.parent.deiconify()
        self.destroy()