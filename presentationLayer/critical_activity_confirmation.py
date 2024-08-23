from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class Confirmation(Frame):
    def __init__(self, window, view):
        super().__init__(window)
        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text='Critical Activity Confirmation', font=("Arial", 13, "bold"))
        self.header.grid(row=0, column=1, pady=10, sticky='w')

        self.username_label = Label(self, text='username')
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.password_label = Label(self, text='password')
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

        self.password_entry = Entry(self, show='*')
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

        self.login_button = Button(self, text='Confirmation', command=self.confirmation)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky='w')

    def confirmation(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_business = UserBusinessLogic()
        response = user_business.login(username, password)
        if not response.success:
            Messagebox.show_error(response.message, f'Error {response.response_code}')
        elif response.data.role_id == 2:
            self.clear_username_password()
            self.main_view.switch_frame('user_management')
        else:
            Messagebox.show_error('You Are Not Allowed To Change the Status.', 'Access Denied')

    def clear_username_password(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
