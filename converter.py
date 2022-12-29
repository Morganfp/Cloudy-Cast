'''
This file contains the conversion functions
The program converts between image formats by utilizing the cv2 library
The program converts between video formats by utilizing the MoviePy library
'''


# Import the necessary libraries
from tkinter import filedialog, Label
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import time



# Function to convert .jpg to .png
def jpg_to_png(root):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Store the selected file name in the filename variable
    # Only .jpg and .jpeg files can be selected as specified by the filestypes paramater
    filename = filedialog.askopenfilename(initialdir=os.path.join(home_dir, 'Desktop'), title="Select A File", filetypes=[("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")])
    # If a file was selected
    if filename:
        # Create a label widget to display a message informing the user that the file is being converted
        converting_label = Label(root, text="Converting...")
        converting_label.configure(bg='#A7D6F0', fg="#383838")
        converting_label.place(relx=0.5, y=185, anchor='center')
        root.update()
        # Images convert fast so pause the program for half a second to allow the messge to be read
        time.sleep(.5)

        # Read the jpg file and store it in the img variable
        img = cv2.imread(filename)
        # Store the file name without the complete path in image_name
        image_name = os.path.basename(filename)
        # Store the image name without the file extension in image_name_without_ext
        image_name_without_ext, file_ext = os.path.splitext(image_name)

        # Save the converted file as "modiefied{i}_image_name_without_ext.png" so that no two files in the users downloads folder have the same name
        i = 1
        while True:
            # The file will start with modified{i} based on the iteration
            file_name = 'modified{}_{}.png'.format(i, image_name_without_ext)
            file_path = os.path.join(home_dir, 'Downloads', file_name)
            # If the file name doesn't exist, save the new file
            if not os.path.exists(file_path):
                cv2.imwrite(file_path, img)
                break
            i += 1

        # Remove the converting label from the window
        converting_label.destroy()
        # Create a label widget to display a message informing the user that the conversion was sucessful
        complete_label = Label(root, text="Conversion complete!")
        complete_label.configure(bg='#A7D6F0', fg="#383838")
        complete_label.place(relx=0.5, y=185, anchor='center')
        # Schedule the removal of the label after 2 seconds (2000 milliseconds)
        root.after(2000, complete_label.destroy)



# Function to convert .png to .jpg
def png_to_jpg(root):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Store the selected file name in the filename variable
    # Only .png files can be selected as specified by the filestypes paramater
    filename = filedialog.askopenfilename(initialdir=os.path.join(home_dir, 'Desktop'), title="Select A File", filetypes=[("PNG Files", "*.png")])
    # If a file was selected
    if filename:
        # Create a label widget to display a message informing the user that the file is being converted
        converting_label = Label(root, text="Converting...")
        converting_label.configure(bg='#A7D6F0', fg="#383838")
        converting_label.place(relx=0.5, y=185, anchor='center')
        root.update()
        # Images convert fast so pause the program for half a second to allow the messge to be read
        time.sleep(.5)

        # Read the png file and store it in the img variable
        img = cv2.imread(filename)
        # Store the file name without the complete path in image_name
        image_name = os.path.basename(filename)
        # Store the image name without the file extension in image_name_without_ext
        image_name_without_ext, file_ext = os.path.splitext(image_name)
        
        # Save the converted file as "modiefied{i}_image_name_without_ext.jpg" so that no two files in the users downloads folder have the same name
        i = 1
        while True:
            # The file will start with modified{i} based on the iteration
            file_name = 'modified{}_{}.jpg'.format(i, image_name_without_ext)
            file_path = os.path.join(home_dir, 'Downloads', file_name)
            # If the file name doesn't exist, save the new file
            if not os.path.exists(file_path):
                cv2.imwrite(file_path, img)
                break
            i += 1

        # Remove the converting label from the window
        converting_label.destroy()
        # Create a label widget to display a message informing the user that the conversion was sucessful
        complete_label = Label(root, text="Conversion complete!")
        complete_label.configure(bg='#A7D6F0', fg="#383838")
        complete_label.place(relx=0.5, y=185, anchor='center')
        # Schedule the removal of the label after 2 seconds (2000 milliseconds)
        root.after(2000, complete_label.destroy)



# Function to convert .mov to .mp4
def mov_to_mp4(root):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Store the selected file name in the filename variable
    # Only .mov files can be selected as specified by the filestypes paramater
    filename = filedialog.askopenfilename(initialdir=os.path.join(home_dir, 'Desktop'), title="Select A File", filetypes=[("MOV Files", "*.mov")])
    # If a file was selected
    if filename:
        # Create a label widget to display a message informing the user that the file is being converted
        converting_label = Label(root, text="Converting...")
        converting_label.configure(bg='#A7D6F0', fg="#383838")
        converting_label.place(relx=0.5, y=185, anchor='center')
        root.update()

        # Read the mov file and store it in the clip variable
        clip = VideoFileClip(filename)
        # Store the file name without the complete path in video_name
        video_name = os.path.basename(filename)
        # Store the video name without the file extension in video_name_without_ext
        video_name_without_ext, file_ext = os.path.splitext(video_name)

        # Save the converted file as "modiefied{i}_video_name_without_ext.mp4" so that no two files in the users downloads folder have the same name
        i = 1
        while True:
            # The file will start with modified{i} based on the iteration
            file_name = 'modified{}_{}.mp4'.format(i, video_name_without_ext)
            file_path = os.path.join(home_dir, 'Downloads', file_name)
            # If the file name doesn't exist, save the new file
            if not os.path.exists(file_path):
                clip.write_videofile(file_path, audio_codec='aac', codec='libx264')
                break
            i += 1

        # Remove the converting label from the window
        converting_label.destroy()
        # Create a label widget to display a message informing the user that the conversion was sucessful
        complete_label = Label(root, text="Conversion complete!")
        complete_label.configure(bg='#A7D6F0', fg="#383838")
        complete_label.place(relx=0.5, y=185, anchor='center')
        # Schedule the removal of the label after 2 seconds (2000 milliseconds)
        root.after(2000, complete_label.destroy)



# Function to convert .mp4 to .mov
def mp4_to_mov(root):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Store the selected file name in the filename variable
    # Only .mp4 files can be selected as specified by the filestypes paramater
    filename = filedialog.askopenfilename(initialdir=os.path.join(home_dir, 'Desktop'), title="Select A File", filetypes=[("MP4 Files", "*.mp4")])
    # If a file was selected
    if filename:
        # Create a label widget to display a message informing the user that the file is being converted
        converting_label = Label(root, text="Converting...")
        converting_label.configure(bg='#A7D6F0', fg="#383838")
        converting_label.place(relx=0.5, y=185, anchor='center')
        root.update()

        # Read the mp4 file and store it in the clip variable
        clip = VideoFileClip(filename)
        # Store the file name without the complete path in video_name
        video_name = os.path.basename(filename)
        # Store the video name without the file extension in video_name_without_ext
        video_name_without_ext, file_ext = os.path.splitext(video_name)

        # Save the converted file as "modiefied{i}_video_name_without_ext.mov" so that no two files in the users downloads folder have the same name
        i = 1
        while True:
            # The file will start with modified{i} based on the iteration
            file_name = 'modified{}_{}.mov'.format(i, video_name_without_ext)
            file_path = os.path.join(home_dir, 'Downloads', file_name)
            # If the file name doesn't exist, save the new file
            if not os.path.exists(file_path):
                clip.write_videofile(file_path, audio_codec='aac', codec='libx264')
                break
            i += 1

        # Remove the converting label from the window
        converting_label.destroy()
        # Create a label widget to display a message informing the user that the conversion was sucessful
        complete_label = Label(root, text="Conversion complete!")
        complete_label.configure(bg='#A7D6F0', fg="#383838")
        complete_label.place(relx=0.5, y=185, anchor='center')
        # Schedule the removal of the label after 2 seconds (2000 milliseconds)
        root.after(2000, complete_label.destroy)



# Function to convert .mkv to .mp4
def mkv_to_mp4(root):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Store the selected file name in the filename variable
    # Only .mkv files can be selected as specified by the filestypes paramater
    filename = filedialog.askopenfilename(initialdir=os.path.join(home_dir, 'Desktop'), title="Select A File", filetypes=[("MKV Files", "*.mkv")])
    # If a file was selected
    if filename:
        # Create a label widget to display a message informing the user that the file is being converted
        converting_label = Label(root, text="Converting...")
        converting_label.configure(bg='#A7D6F0', fg="#383838")
        converting_label.place(relx=0.5, y=185, anchor='center')
        root.update()

        # Read the mkv file and store it in the clip variable
        clip = VideoFileClip(filename)
        # Store the file name without the complete path in video_name
        video_name = os.path.basename(filename)
        # Store the video name without the file extension in video_name_without_ext
        video_name_without_ext, file_ext = os.path.splitext(video_name)

        # Read in the audio from the .mkv file using AudioFileClip
        audio = AudioFileClip(filename)
        # Set the audio for the .mp4 video to the audio from the .mkv file
        clip.set_audio(audio)

        # Save the converted file as "modiefied{i}_video_name_without_ext.mp4" so that no two files in the users downloads folder have the same name
        i = 1
        while True:
            # The file will start with modified{i} based on the iteration
            file_name = 'modified{}_{}.mp4'.format(i, video_name_without_ext)
            file_path = os.path.join(home_dir, 'Downloads', file_name)
            # If the file name doesn't exist, save the new file
            if not os.path.exists(file_path):
                clip.write_videofile(file_path, audio=True, audio_codec='aac', codec='libx264', verbose=True)
                break
            i += 1

        # Remove the converting label from the window
        converting_label.destroy()
        # Create a label widget to display a message informing the user that the conversion was sucessful
        complete_label = Label(root, text="Conversion complete!")
        complete_label.configure(bg='#A7D6F0', fg="#383838")
        complete_label.place(relx=0.5, y=185, anchor='center')
        # Schedule the removal of the label after 2 seconds (2000 milliseconds)
        root.after(2000, complete_label.destroy)
