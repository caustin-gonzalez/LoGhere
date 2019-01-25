import tkinter

# Window for the voice synthesis GUI
class SynthWindow(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.title("LoGhere voice synthesis")
        self.geometry("600x600")
