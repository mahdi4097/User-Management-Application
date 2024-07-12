from presentationLayer.window import Window
from presentationLayer.login import LoginFrame


class MainView:
    def __init__(self):
        self.window = Window()

        self.frames = {}
        self.add_frame('login', LoginFrame(self.window))

        self.window.mainloop()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky='news')
