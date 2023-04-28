import sys
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(f'{title}')

        self.title_var = tk.StringVar()
        self.description_var = tk.StringVar()

        self.technologies = {
            'Python': (tk.IntVar(), '- [Python](https://www.python.org)\n'),
            'Tkinter': (tk.IntVar(), '- [Tkinter](https://docs.python.org/3/library/tkinter.html)\n'),
            'Javascript': (tk.IntVar(), '- [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)\n'),
            'Node': (tk.IntVar(), '- [Node.js](https://nodejs.org)\n'),
            'React': (tk.IntVar(), '- [React.js](https://reactjs.org)\n'),
            'Next': (tk.IntVar(), '- [Next.js](https://nextjs.org)\n'),
            'Vite': (tk.IntVar(), '- [Vite.js](https://vitejs.dev)\n'),
            'Tailwind CSS': (tk.IntVar(), '- [Tailwind CSS](https://tailwindcss.com)\n'),
        }

        self.has_technologies = False

        self.generate_layout()

        self.mainloop()

    def generate_layout(self):
        self.title_entry = ttk.Entry(self, textvariable=self.title_var)
        self.description_entry = ttk.Entry(
            self, textvariable=self.description_var)

        self.configure_technologies_frame()

        for index, technology in enumerate(self.technologies):
            self.create_checkbutton(
                self.technologies_frame,
                technology,
                self.technologies.get(technology)[0]
            ).grid(column=index % 3, row=index//3)

        self.generate_button = ttk.Button(
            self, text='Generate', command=self.generate_md)

        self.title_entry.pack()
        self.description_entry.pack()
        self.technologies_frame.place(
            relx=0.5, rely=0.5, anchor='center')
        self.generate_button.pack()

    def configure_technologies_frame(self):
        self.technologies_frame = ttk.Frame(self)
        self.technologies_frame.grid_columnconfigure(
            (0, 1, 2), weight=1, uniform='1')
        self.technologies_frame.grid_rowconfigure(
            (0, 1, 2, 3, 4), weight=1)

    def create_checkbutton(self, parent, text, variable):
        return ttk.Checkbutton(parent,
                               text=text, variable=variable)

    def generate_md(self):
        title = self.title_var.get()
        description = self.description_var.get()

        file = open('README.md', 'w', encoding='UTF-8')
        file.write(f'# {title}\n\n')
        file.write(f'{description}\n\n')

        technology_counter = 0
        for technology in self.technologies:
            value = self.technologies[technology]

            print(value[0].get())
            if value[0].get():
                technology_counter += 1

        if technology_counter != 0:
            self.has_technologies = True
        else:
            self.has_technologies = False

        if self.has_technologies:
            file.write('## 💻Frameworks/Languages\n\n')

            for technology in self.technologies:
                value = self.technologies[technology]

                if (value[0].get()):
                    file.write(value[1])

        file.close()


app = App((800, 600), 'MD Maker')
