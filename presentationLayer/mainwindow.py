from ttkbootstrap import Window


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.style.theme_use('darkly')
        self.title('User Management Application')
        self.geometry('400x300')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def show_form(self):
        self.mainloop()
