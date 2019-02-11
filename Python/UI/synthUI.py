import tkinter

# Window for the voice synthesis GUI
class SynthWindow(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.title("LoGhere voice synthesis")

testWindow = SynthWindow(None)

# Create a canvas
synthCanvas = tkinter.Canvas(testWindow, bg="white", height=600, width=600)
synthCanvas.pack()

tkinter.mainloop()