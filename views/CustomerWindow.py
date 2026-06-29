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


class CustomerWindow(ctk.CTkToplevel):
    def __init__(self, parent, customer):
        super().__init__(parent)
        self.customer = customer

        self.welcomeMessage = ctk.CTkLabel(self, text=f"Seja bem-vindo, {customer.getName().capitalize()}")
        self.welcomeMessage.pack(pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self, 
            width=250, 
            height=250
        )
        self.scroll_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.title("Área do cliente")
        self.geometry("800x600")

        self.cartButton = ctk.CTkButton(self, text="Carrinho", command=self.openCart)
        self.cartButton.pack(pady=10)
        self.cartButton.place(relx=1.0, rely=0.03, anchor="ne")

        API_KEY = "084b3a88870b7e6b13eb20b3d00c5c54"
        response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}")
        data = response.json()
        movies = data["results"]  # list of movies

        for i, movie in enumerate(movies):
            poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            movie_name = movie["title"]

            response = requests.get(poster_url)
            img = Image.open(BytesIO(response.content))
            ctk_image = ctk.CTkImage(img, size=(150, 220))

            frame = ctk.CTkFrame(self.scroll_frame)
            frame.grid(row=i // 4, column=i % 4, padx=10, pady=10)

            label = ctk.CTkLabel(frame, image=ctk_image, text="")
            label.pack()

            button = ctk.CTkButton(frame, text=movie_name, command=partial(self.openMovieWindow, movie))
            button.pack(pady=5)

    def openCart(self):
        pass

    def openMovieWindow(self, movie):
        self.withdraw()
        MovieWindow(self, movie, self.customer)