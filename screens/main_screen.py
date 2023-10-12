from tkinter import *

from constants import *
from .widgets import button, destroy_widgets

def main_screen(window):
    '''Main Screen'''
    
    # Destroy unnecessary widgets
    destroy_widgets(window)
    
    main = Frame(master=window, bg=BG_COLOR)
    main.pack()
    
    label = Label(master=main, text='Welcome', bg=BG_COLOR)
    label.grid(row=0, column=0)
    
    
    
    