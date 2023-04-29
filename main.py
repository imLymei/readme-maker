import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(f'{title}')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        self.initialize_variables()

        self.generate_layout()

        self.bind_all('<Return>', lambda event: self.generate_md())

        self.mainloop()

    def initialize_variables(self):
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

        self.has_online_access = [tk.IntVar(), tk.StringVar()]

    def generate_layout(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.columnconfigure(0, weight=1, uniform='a')
        self.main_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        self.configure_header()

        self.configure_technologies()

        self.configure_access_options()

        self.generate_button = ttk.Button(
            self.main_frame,
            text='Generate',
            command=self.generate_md
        )

        default_pad_y = 20
        self.main_frame.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.8,
            relheight=0.8,
            anchor='center'
        )
        self.header.grid(column=0, row=0, sticky='nswe')
        self.online_frame.grid(column=0, row=1, sticky='nswe')
        self.technologies_frame.grid(column=0, row=2, sticky='nswe')
        self.generate_button.grid(column=0, row=3, sticky='nswe', pady=10)

    def configure_header(self):
        self.header = ttk.Frame(self.main_frame)

        self.title_frame = self.configure_grid_frame(3, 1, self.header)
        self.title_entry = ttk.Entry(
            self.title_frame,
            textvariable=self.title_var
        )
        self.title_label = ttk.Label(
            self.title_frame,
            text='Titulo',
            width=1
        )

        self.description_frame = self.configure_grid_frame(3, 1, self.header)
        self.description_entry = ttk.Entry(
            self.description_frame,
            textvariable=self.description_var
        )
        self.description_label = ttk.Label(
            self.description_frame,
            text='Descrição',
            width=1
        )

        self.title_label.grid(column=0, row=0, sticky='we')
        self.description_label.grid(column=0, row=0, sticky='we')
        self.title_entry.grid(
            column=1,
            row=0,
            columnspan=5,
            sticky='nswe',
        )
        self.description_entry.grid(
            column=1,
            row=0,
            columnspan=5,
            sticky='nswe',
        )
        self.title_frame.pack(fill='both')
        self.description_frame.pack(fill='both')

    def configure_technologies(self, technologies_columns=3):
        self.technologies_frame = self.configure_grid_frame(
            technologies_columns,
        )

        for index, technology in enumerate(self.technologies):
            ttk.Checkbutton(
                self.technologies_frame,
                text=technology,
                variable=self.technologies.get(technology)[0]
            ).grid(column=index % technologies_columns, row=index//technologies_columns, sticky='nswe')

    def configure_access_options(self):
        self.online_frame = self.configure_grid_frame(
            3,
            row_size=1,
            parent=self.main_frame
        )

        self.online_checkbutton = ttk.Checkbutton(
            self.online_frame,
            text='Online access',
            variable=self.has_online_access[0],
            command=lambda: self.handle_entry_by_checkbutton(
                self.has_online_access[0], self.online_access_entry)
        )
        self.online_access_entry = ttk.Entry(
            self.online_frame,
            textvariable=self.has_online_access[1]
        )
        self.online_access_entry.configure(state='disabled')

        self.online_checkbutton.grid(column=0, row=0, sticky='we')
        self.online_access_entry.grid(
            column=1,
            row=0,
            columnspan=3,
            sticky='we'
        )

    def configure_grid_frame(self, column_size, row_size=5, parent=None):
        if parent == None:
            parent = self.main_frame
        frame = ttk.Frame(parent)
        frame.grid_columnconfigure(
            ([i for i in range(column_size)]), weight=1, uniform='a')
        frame.grid_rowconfigure(
            ([i for i in range(row_size)]), weight=1)
        return frame

    def handle_entry_by_checkbutton(self, checkbutton_var, entry):
        if checkbutton_var.get():
            entry.configure(state='normal')
        else:
            entry.configure(state='disabled')

    def generate_md(self):
        title = self.title_var.get()
        description = self.description_var.get()

        if self.text_is_valid(title) and self.text_is_valid(description):
            file = open('README.md', 'w', encoding='UTF-8')
            file.write(f'# {title}\n\n')
            file.write(f'{description}\n\n')

            if self.has_technologies():
                file.write('## 💻Frameworks/Languages\n\n')

                for technology in self.technologies:
                    value = self.technologies[technology]

                    if (value[0].get()):
                        file.write(value[1])

            file.write("\n## 🚀How to use it?\n\n")

            if self.has_online_access[0].get():
                file.write("### Online access\n\n")
                file.write(
                    f"Just click in the website of the repository or [here]( {self.has_online_access[1].get()} )!\n\n")
                file.write("##### or\n\n")

            file.write("### Local access\n\n")

            if self.technologies['Python'][0].get() or self.technologies['Tkinter'][0].get():
                file.write(
                    "Run the main.py:\n```bash\npython3 main.py\n```\n\n")
                file.write("##### [Back to the top](#)\n\n")
                file.write(
                    "###### Create by [Felipe Cardoso](https://lymei.art)")
            elif self.has_react() or self.has_javascript():
                if self.has_react():
                    start_server = 'npm start'
                else:
                    start_server = 'node .'

                file.write(
                    "Install node modules in the project and start the application:\n")
                file.write(
                    f"\n```bash\n# install npm\nnpm install\n\n# start application\n{start_server}\n```\n\n"
                )
                file.write("##### [Back to the top](#)\n\n")
                file.write(
                    "###### Create by [Felipe Cardoso](https://lymei.art)")

            file.close()
        else:
            self.show_error(
                'Titulo e Descrição precisam conter pelo menos 4 caracteres')

    def text_is_valid(self, text):
        if len(text) > 3:
            return True
        else:
            return False

    def has_technologies(self):
        technology_counter = 0

        for technology in self.technologies:
            value = self.technologies[technology]

            if value[0].get():
                technology_counter += 1

        if technology_counter != 0:
            return True
        else:
            return False

    def has_react(self):
        if self.technologies['Vite'][0].get() or self.technologies['Next'][0].get() or self.technologies['React'][0].get():
            return True
        else:
            return False

    def has_javascript(self):
        if self.technologies['Javascript'][0].get() or self.technologies['Node'][0].get():
            return True
        else:
            return False

    def show_error(self, message):
        messagebox.showerror(
            'Erro na criação do README', message)


app = App((400, 400), 'README Maker')
