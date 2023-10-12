from tkinter import *

from constants import *
from .widgets import button, destroy_widgets, canvas
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
    canvas_widget = canvas(master=splash)
    canvas_widget.create_image(250, 250, image=splash_image)
    canvas_widget.grid(row=0, column=0)
    
    get_started_button = button(master=splash, text='Get Started ->', click=lambda: main_screen(window), justify='center')
    get_started_button.grid(row=1, column=0)
    