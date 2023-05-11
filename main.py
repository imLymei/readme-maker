import markdown
import settings
import elements
import md_generator as mg
import customtkinter as ctk
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(f'{title}')
        self.resizable(False, False)

        self.md_generator = mg.MdGenerator()

        self.add_text(1, 'Meu Titulo')
        self.add_text(2, 'Meu SubTitulo')
        self.add_text(3, 'Um Paragrafo')

        self.bind_all('<Return>', lambda event: self.generate_md())

        self.mainloop()

    def add_text(self, title_importance, text):
        self.md_generator.add_element(elements.Text(title_importance, text))

    def generate_md(self):
        self.md_generator.create_md()


app = App((1280, 720), 'README Maker')
