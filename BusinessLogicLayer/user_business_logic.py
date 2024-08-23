from CommonLayer.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
import bcrypt
from CommonLayer.general_decorators import performance_logger_decorator
from CommonLayer.user import User


class UserBusinessLogic:
	def __init__(self):
		self.user_data_access = UserDataAccess()

	@performance_logger_decorator
	def login(self, username, password):
		if len(username) < 3 or len(password) < 6:
			return Response(None, False, 101, "Invalid Data.")

		user = self.user_data_access.get_user_with_username_password(username, password)

		if not user:
			return Response(None, False, 102, 'Invalid username or password.')

		if not user.active:
			return Response(None, False, 103, 'Your username is not active.')

		return Response(user, True, 201)

	@performance_logger_decorator
	def search(self, search_value, current_user):
		if current_user.role_id == 2:
			search_result_list = self.user_data_access.search_firstname_lastname_username(search_value, current_user)
			return search_result_list

	@performance_logger_decorator
	def get_users(self, current_user):
		if current_user.role_id == 2:
			user_list = self.user_data_access.get_users_except_current_user(current_user.id)
			return user_list

	@performance_logger_decorator
	def activate(self, user_id, current_user):
		if current_user.role_id == 2:
			self.user_data_access.update_active_value(user_id, 1)

	@performance_logger_decorator
	def deactivate(self, user_id, current_user):
		if current_user.role_id == 2:
			self.user_data_access.update_active_value(user_id, 0)

	@performance_logger_decorator
	def check_new_user_entries(self, firstname, lastname, username, password):
		try:
			User(None, firstname, lastname, username, password, None, None)
		except ValueError as error:
			return Response(None, False, error.args[0], error.args[1])

		finally:
			check_username_existence = self.user_data_access.check_username_existence(username)
			if check_username_existence:
				return Response(None, False, 107, f'Someone with username {username} exists.')

		return Response(None, True, 202, f'{firstname.title()} {lastname.title()} registered successfully.')

	@performance_logger_decorator
	def register_new_user(self, firstname, lastname, username, password):
		new_user_firstname = firstname.title()
		new_user_lastname = lastname.title()
		new_user_username = username.lower()
		hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

		self.user_data_access.register_new_user(
				new_user_firstname, new_user_lastname, new_user_username, hashed_password
				)

	@staticmethod
	def text_input_validator(pressed_key):
		if pressed_key.replace(" ", "").isalpha() or pressed_key == "":
			return True
		else:
			return False
