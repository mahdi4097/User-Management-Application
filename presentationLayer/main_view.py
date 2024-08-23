from presentationLayer.mainwindow import MainWindow
from presentationLayer.login import LoginFrame
from presentationLayer.register import RegisterFrame
from presentationLayer.home import HomeFrame
from presentationLayer.user_management import UserManagementFrame
from presentationLayer.critical_activity_confirmation import Confirmation
from CommonLayer.general_decorators import performance_logger_decorator


class MainView:
    def __init__(self):
        # NOTE: self: <presentationLayer.main_view.MainView object at 0x0000023ABB5C7890>
        self.window = MainWindow()  # NOTE: self.window: <presentationLayer.window.MainWindow object .>
        self.frames = {}
        self.add_frame('critical_activity_confirmation', Confirmation(self.window, self))
        self.add_frame('user_management', UserManagementFrame(self.window, self))
        self.add_frame('home', HomeFrame(self.window, self))
        self.add_frame('register', RegisterFrame(self.window, self))
        self.add_frame('login', LoginFrame(self.window, self))
        self.window.show_form()

    @performance_logger_decorator
    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky='news')

    @performance_logger_decorator
    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        # NOTE: The changes in the frame depend on the form being called.
        return frame  # NOTE: This return is used in LoginFrame class to set current user in HomeFrame.

