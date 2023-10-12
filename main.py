from tkinter import *
from constants import *
from screens.splash_screen import splash_screen

window = Tk()

icon = PhotoImage(file='images/icon.png')
window.iconphoto(True, icon)

window.title('MarkMyFrame- An Image Watermarking App by Joboy-dev')
window.minsize(width=850, height=800)
window.maxsize(width=850, height=800)
window.config(bg=BG_COLOR, padx=40, pady=20)

# initialize app by loading up the splash screen
splash_screen(window=window)

window.mainloop()