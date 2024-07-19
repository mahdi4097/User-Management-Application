class User:
    def __init__(self, id, firstname, lastname, username, password, active):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.active = True if active == 1 else False

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
