from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class RegisterFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.new_user = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.main_view = view

        self.header = Label(self, text='Register Form', font=("Arial", 13, "bold"))
        self.header.grid(row=0, column=1, pady=10, sticky='w')

        self.firstname_label = Label(self, text='First Name')
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

        text_validator = (self.register(self.new_user.text_input_validator), '%P')
        self.firstname_entry = Entry(self, validate='key', validatecommand=text_validator)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.lastname_label = Label(self, text='Last Name')
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

        self.lastname_entry = Entry(self, validate='key', validatecommand=text_validator)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.username_label = Label(self, text='username')
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky='e')

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.password_label = Label(self, text='password')
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky='e')

        self.password_entry = Entry(self, show='*')
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.register_button = Button(self, text='Register', command=self.register_new_user)
        self.register_button.grid(row=5, column=1, pady=(0, 10), sticky='w')

        self.login_button = Button(self, text='Login', command=self.show_login_frame)
        self.login_button.grid(row=6, column=1, pady=(0, 10), sticky='w')

    def show_login_frame(self):
        self.main_view.switch_frame('login')

    # noinspection PyArgumentList
    def register_new_user(self):
        self.firstname_entry.config(bootstyle='primary')
        self.lastname_entry.config(bootstyle='primary')
        self.username_entry.config(bootstyle='primary')
        self.password_entry.config(bootstyle='primary')
        new_firstname = self.firstname_entry.get()
        new_lastname = self.lastname_entry.get()
        new_username = self.username_entry.get()
        new_password = self.password_entry.get()

        response = self.new_user.check_new_user_entries(new_firstname, new_lastname, new_username, new_password)

        if not response.success:
            Messagebox.show_error(response.message, f'Error {response.response_code}')
            if response.response_code == 104:
                self.firstname_entry.config(bootstyle='danger')
            elif response.response_code == 105:
                self.lastname_entry.config(bootstyle='danger')
            elif response.response_code in [106, 107]:
                self.username_entry.config(bootstyle='danger')
            else:
                self.password_entry.config(bootstyle='danger')
        else:
            self.new_user.register_new_user(new_firstname, new_lastname, new_username, new_password)
            Messagebox.show_info(response.message, 'Successful Registration')
            self.firstname_entry.delete(0,'end')
            self.firstname_entry.focus()
            self.lastname_entry.delete(0,'end')
            self.username_entry.delete(0,'end')
            self.password_entry.delete(0,'end')
