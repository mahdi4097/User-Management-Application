from presentationLayer.window import Window
from presentationLayer.login import LoginFrame
from presentationLayer.register import RegisterFrame


class MainView:
    def __init__(self):
        self.window = Window()

        self.frames = {}
        self.add_frame('register', RegisterFrame(self.window))
        self.add_frame('login', LoginFrame(self.window, self))

        self.window.mainloop()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky='news')

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
