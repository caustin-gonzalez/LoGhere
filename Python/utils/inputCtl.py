import tkinter
from vsynth.vars import *

class MouseController:

  # When a new instance of this class is created, return a reference to self so that functions from it can be called.
  def __new__(self):
    return self

  # Unknown purpose - count the number of touches and how long it's been held down for?
  self.touches_with_mouse = []
  self.mouse_touch = {
    "alive": False,
    "end_time": 0
    }

  # Bind left mouse-click to start_touches function
  # Might not be necessary as the 'touchstart' and other 'touch...' event listeners in JS
  # are only for touchscreens
  self.bind("<Button-1>",self.start_touches)
  
  # The function called when the left mouse click is caught by the listener.
  # This sets the mouse as down, to allow tracking for how long it is held down.
  def mouse_clickdown(event):
    self.mouse_down = True
    self.start_mouse(event)
    
  def mouse_unclick(event):
    self.mouse_down = False
    self.end_mouse(event)
    
  def start_mouse(event):
    if audioSystem.started == False:
      audioSystem.started = True
      audioSystem.start_sound()

    touch = {}
    touch.startTime = time

  def end_mouse(event):
    # wip
  
  # Detect when the left mouse button is pressed
  self.bind("<Button-1>",self.mouse_clickdown(event))
            
  # Detect when the left mouse button is released
  self.bind("<ButtonRelease-1>",self.mouse_unclick(event))

  # Get coordinates of the mouse pointer relative to the root window.
  self.mouseX = self.winfo_pointerx()
  self.mouseY = self.winfo_pointery()
