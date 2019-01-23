import tkinter

# Window for the voice synthesis GUI
class SynthWindow(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.title("LoGhere voice synthesis")
        self.geometry("600x600")
        
        # Unknown purpose - count the number of touches and how long it's been held down for?
        self.touches_with_mouse = []
        self.mouse_touch = {
            "alive": false,
            "end_time": 0
        }
        
        # Bind left mouse-click to start_touches button
        self.bind("<Button-1>",self.start_touches)
        
        # Coordinates of the mouse pointer relative to the root window.
        self.mouseX = self.winfo_pointerx()
        self.mouseY = self.winfo_pointery()
