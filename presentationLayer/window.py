from tkinter import Tk


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('User Management Application')
        self.geometry('400x300')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def show_form(self):
        self.mainloop()
