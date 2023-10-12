import random
import os

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

from constants import *
from .widgets import button, destroy_widgets, label, canvas

allowed_formats = ['jpg', 'png', 'jpeg', 'jfif']
watermarked_image = None

def open_image_file():
    '''Function to open and select a file'''
    
    global image_file_path
    image_file_path = filedialog.askopenfilename().lower()
    print(image_file_path)
    
    for pic in allowed_formats:
        if pic in image_file_path:
            show_widgets()
            break
        else:
            # display error message
            messagebox.showerror(title='Error', message=f'Invalid file format. Allowed formats are: \njpg, png, jpeg, jfif.')
            break


def apply_watermark(text):
    '''Function to apply watermark to image'''
    
    image = Image.open(fp=image_file_path).convert(mode='RGBA')
    
    watermark = Image.new(mode="RGBA", size=image.size, color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)
    
    w, h = image.size
    x, y = int(w / 2), int(h / 2)
    
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
        
    font = ImageFont.truetype("arial.ttf", int(font_size/6))
    
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 170), anchor='ms')
    
    global watermarked_image
    watermarked_image = Image.alpha_composite(image, watermark)
    
    global watermark_applied_text_label
    watermark_applied_text_label.config(text='Watermark applied to image.')
    
    # Preview image
    # if watermarked_image is not None:
    #     photo = ImageTk.PhotoImage(image=watermarked_image)
    #     canvas_widget = canvas(master=main)
    #     canvas_widget.create_image(250, 250, image=photo)
    #     canvas_widget.grid(row=7, column=0)


def save_image():
    '''Function to save image'''
    
    global watermarked_image
    
    if watermarked_image is not None:
        file = image_file_path.split('/')[-1]
        rand_id = random.randint(1000, 10000000)
        
        # Get the directory where the script is located
        script_directory = os.path.dirname(os.path.realpath(__file__))
        file_name = f'{file}-MarkMyFrame_{rand_id}.png'
        
        save_path = os.path.join(script_directory, file_name)
        
        watermarked_image.save(fp=save_path)
        
        global file_saved_text_label
        file_saved_text_label.config(text='Watermarked image saved.')
    else:
        messagebox.showerror(title='Error', message=f'Watermark has not beeen applied to image. Click button to apply watermark and try saving image again.')
    
    
def show_widgets():
    '''Function to show remainig widget elements'''
    
    global main
        
    global watermark_text_input
    watermark_text = watermark_text_input.get()
    
    if watermark_text:
        global selected_file_label
        selected_file_label.config(text=image_file_path.split('/')[-1])
        
        apply = button(master=main, text='Apply Watermark', click=lambda: apply_watermark(text=watermark_text))
        apply.grid(row=5, column=0)
        
        save_file_button = button(master=main, text='Save File', click=save_image)
        save_file_button.grid(row=5, column=1)
    else:
        messagebox.showwarning(title='Empty field.', message='Please fill in the Watermark Text Field.')


def main_screen(window):
    '''Main Screen'''
    
    # Destroy unnecessary widgets
    destroy_widgets(window)
    
    global main
    main = Frame(master=window, bg=BG_COLOR)
    main.pack()
    
    welcome_label = label(master=main, text='Welcome to MarkMyFrame', justify='right', fg_color=PRIMARY_COLOR)
    welcome_label.grid(row=0, column=1)
    
    info_label = label(master=main, text='Enter what you want to appear as the watermark text and\n click the button below to select an image file.', justify='right')
    info_label.grid(row=1, column=1)
    
    watermark_text_label = label(master=main, text='Enter Watermark Text: ')
    watermark_text_label.grid(row=2, column=0)
    
    global watermark_text_input
    watermark_text_input = Entry(master=main, bg=BG_COLOR, fg=PRIMARY_COLOR, width=50, font=TEXT_FONT_SPECS, highlightcolor=PRIMARY_COLOR)
    watermark_text_input.grid(row=2, column=1, columnspan=2)
    watermark_text_input.focus()
    
    select_file_button = button(master=main, text='Select File', click=open_image_file)
    select_file_button.grid(row=3, column=1)
    
    global selected_file_label
    selected_file_label = label(master=main, text='', fg_color=SECONDARY_COLOR)
    selected_file_label.grid(row=4, column=1)
    
    global watermark_applied_text_label
    watermark_applied_text_label = label(master=main, text='', fg_color=SECONDARY_COLOR)
    watermark_applied_text_label.grid(row=6, column=0)
    
    global file_saved_text_label
    file_saved_text_label = label(master=main, text='', fg_color=SECONDARY_COLOR)
    file_saved_text_label.grid(row=6, column=1)
