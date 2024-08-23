class User:
	def __init__(self, id, firstname, lastname, username, password, active, role_id):
		self.id = id
		self.first_name = firstname
		self.last_name = lastname
		self.username = username
		self.password = password
		self.active = True if active == 1 else False
		self.role_id = role_id

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str) or len(value) < 2 or len(value) > 50:
			raise ValueError(104, 'Invalid First Name!')
		self._first_name = value

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, value):
		if not isinstance(value, str) or len(value) < 2 or len(value) > 100:
			raise ValueError(105, 'Invalid Last Name!')
		self._last_name = value

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, value):
		if not isinstance(value, str) or len(value) < 3:
			raise ValueError(106, 'Invalid username!\nusername must be at least 3 characters.')
		self._username = value

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, value):
		if value is not None and len(value) < 6:
			raise ValueError(108, 'Invalid password!\npassword must be at least 6 characters.')
		self._password = value

	def get_fullname(self):
		return f'{self.first_name} {self.last_name}'
