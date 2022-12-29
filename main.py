"""
This file contains the main function and front-end design of the application including the application window and widgets
"""


# Import the necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Label
import converter



# Function to call a conversion function based of user selection
def file_selector():
    if clicked.get() == "JPG/JPEG to PNG":
        converter.jpg_to_png(root)

    elif clicked.get() == "PNG to JPG":
        converter.png_to_jpg(root)

    elif clicked.get() == "MOV to MP4":
        converter.mov_to_mp4(root)

    elif clicked.get() == "MP4 to MOV":
        converter.mp4_to_mov(root)

    elif clicked.get() == "MKV to MP4":
        converter.mkv_to_mp4(root)



def main():
    # Create the root window
    global root 
    root = tk.Tk()
    
    # Customize root window display
    # Set the root window background color to an empty string (this will make it transparent)
    root.configure(bg='')
    root.title('CloudyCast')
    root.geometry("400x300")
    # Disable resizing of the window
    root.resizable(False, False)

    # Load the image file
    image = PhotoImage(file='img/bg.png')

    # Create a label widget that displays the image
    label = Label(root, image=image)

    # Place the label widget in the root window
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Gloabal string to hold the user option selected from the dropdown
    global clicked
    clicked = tk.StringVar()
    clicked.set("Choose A Conversion Type")
    
    # List to hold the available conversion types
    options = ["JPG/JPEG to PNG", "PNG to JPG", "MOV to MP4", "MP4 to MOV", "MKV to MP4"]

    # Dropdown menu to display conversion options
    dropdown = tk.OptionMenu(root, clicked, *options)
    dropdown.configure(bg="#A7D6F0", highlightbackground="#FFFFFF", fg="#383838")
    dropdown.place(relx=0.5, y=125, anchor='center')

    # Button to display file dialog box
    file_select_button = tk.Button(root, text="Choose a file", command=file_selector)
    file_select_button.configure(highlightbackground="#A7D6F0", fg="#383838")
    file_select_button.place(x=144, y=140)

    # Main loop of the program
    root.mainloop()



# Call the main function
if __name__ == '__main__':
    main()
