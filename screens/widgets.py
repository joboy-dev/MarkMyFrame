from tkinter import *
from constants import *

def destroy_widgets(window):
    '''Function to destroy unnecessary widgets so as to display a new screen'''
    
    # Destroy or hide the previous screen's widgets
    for widget in window.winfo_children():
        widget.destroy()
        


def button(master, text, click, width=15):
    '''Widget for customizing buttons easily'''
    
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
        pady=10,
        command=click,
    )