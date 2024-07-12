import sqlite3
from CommonLayer.user import User


class UserDataAccess:
    def __init__(self):
        self.database_name = "UserManagementDB.db"

    def get_user_with_username_password(self, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                '''
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password,
                       active
                FROM   User
                WHERE  username=?
                And    password=?
                            ''', [username, password]
            ).fetchone()
        if data:
            user = User(data[0], data[1], data[2], data[3], data[4], data[5])
            return user
