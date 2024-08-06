from CommonLayer.response import Response
from DataAccessLayer.user_data_access import UserDataAccess


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 6:
            return Response(None, False, 101, "Invalid Data.")

        user = self.user_data_access.get_user_with_username_password(username, password)

        if not user:
            return Response(None, False, 102, 'Invalid username or password.')

        if not user.active:
            return Response(None, False, 103, 'Your username is not active.')

        return Response(user, True, 201)

    def search(self, search_value, current_user):
        if current_user.role_id == 2:
            search_result_list = self.user_data_access.search_firstname_lastname_username(search_value, current_user)
            return search_result_list

    def get_users(self, current_user):
        if current_user.role_id == 2:
            user_list = self.user_data_access.get_users_except_current_user(current_user.id)
            return user_list

    def activate(self, user_id, current_user):
        if current_user.role_id == 2:
            self.user_data_access.update_active_value(user_id, 1)

    def deactivate(self, user_id, current_user):
        if current_user.role_id == 2:
            self.user_data_access.update_active_value(user_id, 0)

    def check_new_user_entries(self, firstname, lastname, username, password):
        if len(firstname) < 2:
            return Response(None, False, 104, 'Please enter a valid First Name.')

        if len(lastname) < 2:
            return Response(None, False, 105, 'Please enter a valid Last Name.')

        if len(username) < 3:
            return Response(None, False, 106, 'username must be at least 3 characters.')
        else:
            check_username_existence = self.user_data_access.check_username_existence(username)
            if check_username_existence:
                return Response(None, False, 107, f'Someone with username {username} exists.')

        if len(password) < 6:
            return Response(None, False, 108, 'password must be at least 6 characters.')

        return Response(None, True, 202, f'{firstname} {lastname} registered successfully.')

    def register_new_user(self, firstname, lastname, username, password):
        self.user_data_access.register_new_user(firstname, lastname, username, password)

    @staticmethod
    def text_input_validator(pressed_key):
        if pressed_key.replace(" ", "").isalpha() or pressed_key == "":
            return True
        else:
            return False
