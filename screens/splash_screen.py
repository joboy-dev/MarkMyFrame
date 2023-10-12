from tkinter import *

from constants import *
from .widgets import button, destroy_widgets
from .main_screen import main_screen

def splash_screen(window):
    '''Splash Screen'''
    
    # Destroy unnecessary widgets
    destroy_widgets(window)
    
    splash = Frame(master=window, bg=BG_COLOR)
    splash.pack()
    
    # Load image
    splash_image = PhotoImage(master=splash, file='images/logo.png')
    # Store the image as an attribute of the window to prevent it from being garbage collected
    window.splash_image = splash_image
    
    # set up image
    canvas = Canvas(master=splash, height=500, width=500, highlightthickness=0)
    canvas.create_image(250, 250, image=splash_image)
    canvas.grid(row=0, column=0)
    
    get_started_button = button(master=splash, text='Get Started >>', click=lambda: main_screen(window))
    get_started_button.grid(row=1, column=0)
    