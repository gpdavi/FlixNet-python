import customtkinter as ctk
import requests


class ManagerWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.state("zoomed")

        ctk.CTkLabel(
            self,
            text="Seja bem-vindo, administrador.",
            font=("Arial", 20)
        ).pack(pady=10)

        API_KEY = "084b3a88870b7e6b13eb20b3d00c5c54"

        response = requests.get(
            f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
        )

        data = response.json()
        movies = data["results"]

        scroll = ctk.CTkScrollableFrame(self)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        self.movies = {}

        for movie in movies:
            frame = ctk.CTkFrame(scroll)
            frame.pack(fill="x", padx=5, pady=5)

            title = ctk.CTkLabel(frame, text=movie["title"])
            title.pack(side="left", padx=10)

            dots = ctk.CTkLabel(frame, text="." * 200)
            dots.pack(side="left", fill="x", expand=True)

            var = ctk.StringVar(value="Disponível")

            option = ctk.CTkOptionMenu(
                frame,
                values=["Disponível", "Indisponível"],
                variable=var
            )
            option.pack(side="right", padx=10)

            self.movies[movie["title"]] = var

            # cara o manager pode selecionar se o filme tá disponível ou não, mas não tá mudando nada no catálogo