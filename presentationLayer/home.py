from ttkbootstrap import Frame, Label, Button
from icecream import ic


class HomeFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.current_user = None
        self.main_view = view  # NOTE: view: <presentationLayer.main_view.MainView object at 0x00000127E17657F0>

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self)
        self.header.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text='Logout', command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky='ew')

        self.user_management_button = Button(self, text='User Management', command=self.go_user_management)

    def logout(self):
        self.main_view.switch_frame('login')

    def set_current_user(self, user):
        self.current_user = user  # NOTE: user: <CommonLayer.user.User object at 0x000001DAA410EB40>
        self.header.configure(text=f'Welcome {self.current_user.get_fullname()}', font=("Arial", 13, "bold"))
        if self.current_user.role_id == 2:
            self.user_management_button.grid(row=2, column=0, pady=(0, 10), padx=20, sticky='ew')

    def go_user_management(self):
        frame = self.main_view.switch_frame('user_management')
        frame.set_current_user(self.current_user)
