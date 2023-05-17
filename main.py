import settings
import markdown
import tkhtmlview
import md_manager as mg
import customtkinter as ctk
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(f'{title}')
        self.resizable(False, False)

        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='a')

        self.md_manager = mg.MdManager()

        self.html = ''
        self.html_view = tkhtmlview.HTMLScrolledText(master=self, padx=5, pady=5, state='disabled', cursor='arrow',
                                                     html=self.html)
        self.html_view.configure(foreground='#fff', background='#333')
        self.html_view.grid(column=1, row=0, sticky='nswe')
        self.html_view.fit_height()

        self.md_manager.last_added.trace('w', lambda *args: self.update_html_view())

        self.md_manager.add_heading(1, 'My TiTle')
        self.md_manager.add_heading(2, 'My SUBTITLE')
        self.md_manager.add_heading(3, 'My TEST')

        # self.bind_all('<Return>', lambda event: self.generate_md())
        self.bind_all('<Return>', lambda event: self.md_manager.add_paragraph('My TiTle'))

        self.mainloop()

    def update_html_view(self):
        self.html = ''

        for element in self.md_manager.elements:
            self.html += element.markdown

        self.html = markdown.markdown(self.html)

        self.html_view.set_html(self.html)

    def generate_md(self):
        self.md_manager.create_md()


app = App((1280, 720), 'README Maker')
