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
