import sys

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

        self.html = ''

        self.heading_working = True
        self.paragraph_working = True
        self.html_parser_working = True

        self.md_manager = mg.MdManager()

        self.heading_test()

        self.paragraph_test()

        self.html_view_test()

        self.quit()
        sys.exit()

        # self.bind_all('<Return>', lambda event: self.generate_md())

        # self.mainloop()

    def heading_test(self):
        tries_one = -4
        tries_two = 10
        total_tries = abs(tries_two) + abs(tries_one)

        try:
            [self.md_manager.add_heading('d', f'My TiTle number {i}') for i in range(-4, 10)]

            if len(self.md_manager.elements) != total_tries:
                self.heading_working = False

            for elements in self.md_manager.elements:
                if 0 > elements.title_importance > 5:
                    self.heading_working = False
        except:
            self.heading_working = False

        print('Heading working!' if self.heading_working else 'Heading error!')

        self.reset_elements()

    def paragraph_test(self):
        try:
            [self.md_manager.add_paragraph(f'this is text {i:.^{i}}') for i in range(2000)]

            for elements in self.md_manager.elements:
                if len(elements.markdown) <= 4:
                    self.paragraph_working = False
        except:
            self.paragraph_working = False

        print('Paragraph working!' if self.heading_working else 'Paragraph error!')

        self.reset_elements()

    def html_view_test(self):
        try:
            self.update_html_view()
        except:
            self.html_parser_working = False

        print('Html view working!' if self.heading_working else 'Html view error!')

    def update_html_view(self):
        self.html = ''

        for element in self.md_manager.elements:
            self.html += element.markdown

    def reset_elements(self):
        self.md_manager.elements = []


app = App((1280, 720), 'README Maker')
