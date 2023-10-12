from tkinter import *
from constants import *

def destroy_widgets(window):
    '''Function to destroy unnecessary widgets so as to display a new screen'''
    
    # Destroy or hide the previous screen's widgets
    for widget in window.winfo_children():
        widget.destroy()
        


def button(master, text, click, width=15, justify='left'):
    '''Function to display button widget'''
    
    return Button(
        master=master,
        bg=PRIMARY_COLOR, 
        fg=BG_COLOR, 
        activebackground=BG_COLOR,
        activeforeground=SECONDARY_COLOR,
        width=width,
        text=text, 
        font=BUTTON_FONT_SPECS,
        borderwidth=0.1, 
        highlightthickness=0,
        highlightbackground=BG_COLOR,
        pady=5,
        command=click,
        justify=justify
    )
    

def label(master, text, justify='left', fg_color=SECONDARY_COLOR):
    '''Fucntion to display label widget'''
    
    return Label(
        master=master,
        text=text,
        bg=BG_COLOR,
        fg=fg_color,
        font=TEXT_FONT_SPECS,
        pady=10,
        justify=justify,
    )
    

def canvas(master, height=500, width=500):
    '''Function to display canvas'''
    
    return Canvas(master=master, height=height, width=width, highlightthickness=0)