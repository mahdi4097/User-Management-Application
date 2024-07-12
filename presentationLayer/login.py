from tkinter import Frame, Label, Entry, Button


class LoginFrame(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text='Login Form')
        self.header.grid(row=0, column=1, pady=10, sticky='w')

        self.username_label = Label(self, text='username')
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.password_label = Label(self, text='password')
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

        self.password_entry = Entry(self, show='*')
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.login_button = Button(self, text='Login')
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky='w')
