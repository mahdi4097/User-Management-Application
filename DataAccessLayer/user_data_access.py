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
                       active,
                       role_id
                FROM   User
                WHERE  username=?
                And    password=?
                            ''', [username, password]
            ).fetchone()
        if data:
            user = User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            return user

    def get_users_except_current_user(self, current_user_id):
        user_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                '''
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       active,
                       role_id
                FROM   User
                WHERE  id != ?
                            ''', [current_user_id]
            ).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, True if item[4] == 1 else False, item[5])
                user_list.append(user)
        return user_list

    def update_active_value(self, user_id, new_value):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''
                            UPDATE User
                            SET active = ?
                            WHERE id = ? 
                            ''', [new_value, user_id]
            )
            connection.commit()

    def search_firstname_lastname_username(self, search_value, current_user):
        search_result_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                '''
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       active,
                       role_id
                FROM   User
                WHERE  (first_name LIKE ?
                OR        last_name LIKE ?
                OR        username LIKE ?)
                AND        id != ?
                            ''', [f'%{search_value}%', f'%{search_value}%', f'%{search_value}%', current_user.id]
            ).fetchall()

        for item in data:
            user = User(item[0], item[1], item[2], item[3], None, True if item[4] == 1 else False, item[5])
            search_result_list.append(user)
        return search_result_list

    def check_username_existence(self, requested_username):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                '''
                            SELECT     username
                            FROM       User
                            WHERE      username=?
                            ''', [requested_username]
            ).fetchall()
            if data:
                return True

    def register_new_user(self, firstname, lastname, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''
                INSERT INTO User (
                                    first_name,
                                    last_name,
                                    username,
                                    password
                                 )
                VALUES (?,?,?,?)
                                     
                            ''', [firstname, lastname, username, password]
            )

            connection.commit()
            print("User registered successfully.")
