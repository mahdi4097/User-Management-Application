from CommonLayer.response import Response
from DataAccessLayer.user_data_access import UserDataAccess


class UserBusinessLogic:
    def __init__(self):

        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 6:
            return Response(None, False, "Invalid Data.")

        user = self.user_data_access.get_user_with_username_password(username, password)

        if not user:
            return Response(None, False, 'Invalid username or password.')

        if not user.active:
            return Response(None, False, 'Your username is not active.')

        return Response(user, True)

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
