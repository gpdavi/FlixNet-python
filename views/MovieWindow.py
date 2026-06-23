import customtkinter as ctk
from controllers.Application import Application
from models.CustomerArchive import CustomerArchive
from CTkMessagebox import CTkMessagebox
from models.Customer import Customer
from PIL import Image
import requests
from io import BytesIO
from functools import partial

class MovieWindow(ctk.CTkToplevel):
    def __init__(self, parent, movie):
        super().__init__(parent)

        posterUrl = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        movieName = movie["title"]
        movieDescription = movie["overview"]
        movieReleaseDate = movie["release_date"]
        movieRating = movie["vote_average"]

        self.geometry("1000x1000")
        self.title(movieName)

        response = requests.get(posterUrl)
        img = Image.open(BytesIO(response.content))
        ctk_image = ctk.CTkImage(img, size=(450, 450))

        movieFrame = ctk.CTkFrame(self)

        movieFrame.pack()

        movieNameLabel = ctk.CTkLabel(movieFrame, text=movieName, font=("Papyrus", 40, "bold"))
        movieNameLabel.pack(padx=45)

        movieImage = ctk.CTkLabel(movieFrame, image=ctk_image, text="")
        movieImage.pack()

        movieDescriptionLabel = ctk.CTkTextbox(movieFrame, text=f"Descrição: {movieDescription}", font=("Papyrus", 20))
        movieDescriptionLabel.pack(pady=10)

        movieReleaseDateLabel = ctk.CTkLabel(movieFrame, text=f"Data de lançamento: {movieReleaseDate}")
        movieReleaseDateLabel.pack(pady=10)

        movieRatingLabel = ctk.CTkLabel(movieFrame, text=f"Nota: {movieRating}")
        movieRatingLabel.pack(pady=10)
        
        rentButton = ctk.CTkButton(self, text="ALUGAR", command=self.addToCart)
        rentButton.pack()

    def addToCart(self):
        pass