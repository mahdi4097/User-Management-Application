from ttkbootstrap import Frame, Label, Button, Entry, Treeview
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from CommonLayer.general_decorators import confirmation_decorator, performance_logger_decorator


class UserManagementFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view
        self.row_list = []
        self.current_user = None
        self.user_business = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text='User Management Form', font=("Arial", 13, "bold"))
        self.header.grid(row=0, column=0, pady=10)

        self.search_entry = Entry(self, width=30)
        self.search_entry.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='w')

        self.search_button = Button(self, text='Search', command=self.search)
        self.search_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky='e')

        self.active_button = Button(self, text='Active', command=self.activate)
        self.active_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='e')

        self.deactive_button = Button(self, text='Deactive', command=self.deactivate)
        self.deactive_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky='w')

        self.user_table = Treeview(self, columns=('first_name', 'last_name', 'username', 'Status'))
        self.user_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky='news')
        self.user_table.heading('#0', text='No')
        self.user_table.heading('#1', text='First Name')
        self.user_table.heading('#2', text='Last Name')
        self.user_table.heading('#3', text='username')
        self.user_table.heading('#4', text='Status')

    @performance_logger_decorator
    def search(self):
        search_value = self.search_entry.get()
        user_list = self.user_business.search(search_value, self.current_user)
        self.fill_table(user_list)

    @performance_logger_decorator
    @confirmation_decorator
    def activate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.activate(user_id, self.current_user)
        user_list = self.load_data()
        self.fill_table(user_list)

    @performance_logger_decorator
    @confirmation_decorator
    def deactivate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.deactivate(user_id, self.current_user)
        user_list = self.load_data()
        self.fill_table(user_list)

    @performance_logger_decorator
    def set_current_user(self, user):
        self.current_user = user
        user_list = self.load_data()
        self.fill_table(user_list)

    @performance_logger_decorator
    def load_data(self):
        user_list = self.user_business.get_users(self.current_user)
        return user_list

    @performance_logger_decorator
    def fill_table(self, user_list):
        for row in self.row_list:
            self.user_table.delete(row)
        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_table.insert(
                '', 'end', iid=user.id, text=str(row_number),
                values=(user.first_name, user.last_name, user.username, 'Active' if user.active.value else 'Deactive')
            )
            self.row_list.append(row)
            row_number += 1
