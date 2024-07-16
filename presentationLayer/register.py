from tkinter import Frame, Label, Entry, Button


class RegisterFrame(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text='Register Form')
        self.header.grid(row=0, column=1, pady=10, sticky='w')

        self.firstname_label = Label(self, text='First Name')
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.lastname_label = Label(self, text='Last Name')
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.username_label = Label(self, text='username')
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky='e')

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.password_label = Label(self, text='password')
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky='e')

        self.password_entry = Entry(self, show='*')
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.login_button = Button(self, text='Login')
        self.login_button.grid(row=5, column=1, pady=(0, 10), sticky='w')

        self.register_button = Button(self, text='Register')
        self.register_button.grid(row=6, column=1, pady=(0, 10), sticky='w')