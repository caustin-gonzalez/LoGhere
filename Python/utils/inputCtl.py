
class MouseController:
  
  # When a new instance of this class is created, return a reference to self so that functions from it can be called.
  def __new__(self):
    return self

  # Unknown purpose - count the number of touches and how long it's been held down for?
  self.touches_with_mouse = []
  self.mouse_touch = {
    "alive": false,
    "end_time": 0
    }

  # Bind left mouse-click to start_touches function
  master.bind("<Button-1>",self.start_touches)

  # Get coordinates of the mouse pointer relative to the root window.
  master.mouseX = master.winfo_pointerx()
  master.mouseY = master.winfo_pointery()
