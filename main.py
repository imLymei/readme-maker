import settings
import md_manager as mg
import customtkinter as ctk
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(f'{title}')
        self.resizable(False, False)

        self.md_manager = mg.MdManager()
        self.md_manager.add_heading(1, 'My TiTle')
        self.md_manager.add_heading(2, 'My SUBTITLE')
        self.md_manager.add_heading(3, 'My TEST')
        self.md_manager.add_paragraph('Teste Aury')

        self.bind_all('<Return>', lambda event: self.generate_md())

        self.mainloop()

    def generate_md(self):
        self.md_manager.create_md()


app = App((1280, 720), 'README Maker')
