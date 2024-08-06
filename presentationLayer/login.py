from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from icecream import ic


class LoginFrame(Frame):
	def __init__(self, window, view):
		super().__init__(window)
		# NOTE: self: <presentationLayer.login.LoginFrame object .!loginframe>

		self.main_view = view
		# NOTE: self.main_view and view: <presentationLayer.main_view.MainView object at 0x000001EB25207890>

		self.grid_columnconfigure(1, weight=1)

		self.header = Label(self, text='Login Form', font=("Arial", 13, "bold"))
		self.header.grid(row=0, column=1, pady=10, sticky='w')

		self.username_label = Label(self, text='username')
		self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

		self.username_entry = Entry(self)
		self.username_entry.insert(0, 'z.saeidi')
		self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

		self.password_label = Label(self, text='password')
		self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

		self.password_entry = Entry(self, show='*')
		self.password_entry.insert(0, '123456')
		self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky='ew')

		self.login_button = Button(self, text='Login', command=self.login)
		self.login_button.grid(row=3, column=1, pady=(0, 10), sticky='w')

		self.register_button = Button(self, text='Register', command=self.show_register_frame)
		self.register_button.grid(row=4, column=1, pady=(0, 10), sticky='w')

	def show_register_frame(self):
		self.main_view.switch_frame('register')

	def login(self):
		username = self.username_entry.get()
		password = self.password_entry.get()

		user_business = UserBusinessLogic()
		response = user_business.login(username, password)
		if not response.success:
			Messagebox.show_error(response.message, f'Error {response.response_code}')
		else:
			self.clear_username_password()
			home_frame = self.main_view.switch_frame('home')
			home_frame.set_current_user(response.data)
		# NOTE: response.data: <CommonLayer.user.User object at 0x0000025AAD45DE50>

	def clear_username_password(self):
		self.username_entry.delete(0, 'end')
		self.password_entry.delete(0, 'end')
