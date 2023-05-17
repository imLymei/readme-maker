import elements
import tkinter as tk
import settings


class MdManager:
    def __init__(self):
        self.file_name = 'README_TESTE'
        self.directory = './'

        self.last_added = tk.StringVar()

        self.elements = []

    def create_md(self):
        file = open(f'{self.directory}/{self.file_name}.md', 'w', encoding='UTF-8')
        self.add_elements_to_md(file)
        file.close()

    def add_elements_to_md(self, file):
        for element in self.elements:
            file.write(element.markdown)

    def add_element(self, element):
        self.elements.append(element)
        self.last_added.set(element.markdown)

    def add_heading(self, title_importance, text):
        new_text = elements.Heading(title_importance, text)
        self.add_element(new_text)

    def add_paragraph(self, text):
        new_text = elements.Paragraph(text)
        self.add_element(new_text)
