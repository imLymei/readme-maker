import elements
import settings


class MdManager:
    def __init__(self):
        self.file_name = 'README_TESTE'
        self.directory = './'

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

    def add_header(self, title_importance, text):
        new_text = elements.Header(title_importance, text)
        self.add_element(new_text)
