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
    def __init__(self, parent, movie, customer):
        super().__init__(parent)
        self.parent = parent

        self.state("zoomed")
        self.customer = customer
        self.customerCart = customer.getCart()

        posterUrl = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        movieName = movie["title"]
        movieDescription = movie["overview"]
        movieReleaseDate = movie["release_date"]
        movieRating = movie["vote_average"]
        moviePrice = "R$ 10,00"

        self.geometry("1000x1000")
        self.title(movieName)

        response = requests.get(posterUrl)
        img = Image.open(BytesIO(response.content))
        ctk_image = ctk.CTkImage(img, size=(300, 300))

        movieFrame = ctk.CTkFrame(self, height=800, width=800)

        returnButton = ctk.CTkButton(self, text="Voltar", command=self.returnToCatalog, compound="left")
        returnButton.pack(anchor="w")

        movieNameLabel = ctk.CTkLabel(movieFrame, text=movieName, font=("Papyrus", 40, "bold"))
        movieNameLabel.pack(padx=45)

        movieImage = ctk.CTkLabel(movieFrame, image=ctk_image, text="")
        movieImage.pack()

        movieDescriptionLabel = ctk.CTkLabel(movieFrame, text=f"{movieDescription}", font=("Papyrus", 20), wraplength=700)
        movieDescriptionLabel.pack()

        movieReleaseDateLabel = ctk.CTkLabel(movieFrame, text=f"Data de lançamento: {movieReleaseDate}")
        movieReleaseDateLabel.pack()

        movieRatingLabel = ctk.CTkLabel(movieFrame, text=f"Nota: {movieRating}")
        movieRatingLabel.pack()

        moviePriceLabel = ctk.CTkLabel(movieFrame, text=f"Preço: {moviePrice}")

        movieFrame.pack() 
        moviePriceLabel.pack()
        
        rentButton = ctk.CTkButton(movieFrame, text="Alugar", command=partial(self.addToCart, movieName))
        
        rentButton.pack()

    def addToCart(self, movieName):
        self.customer.cartAdd(movieName)
        self.customer.increasePayment()
        CTkMessagebox(title="Carrinho", message=f"{movieName} adicionado ao carrinho!")
        self.returnToCatalog()

    def returnToCatalog(self):
            self.parent.deiconify()
            self.after(50, self.destroy)