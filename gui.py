from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from control import Control

# Gui
class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Media Player Gesture Controller")
        self.root.config(padx=50, bg="#fff")

        self.canvas = Canvas(width=350, height=300, bg="#fff", highlightthickness=0)
        logo_img = ImageTk.PhotoImage(Image.open("media/logo.jpeg"))
        self.canvas.create_image(175, 175, anchor=CENTER, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=1)

        self.media_path_label = Label(text="Select a file to launch the controller. Type 'Q' to quit.",
                                      bg="#fff", fg="#222831", pady=40)
        self.media_path_label.grid(column=0, row=2)

        self.browse = Button(text="Browse", command=self.browsefiles, relief=FLAT, bg="#393e46", fg="#eaeaea",
                             highlightthickness=0)
        self.browse.grid(column=0, row=3, sticky="EW", columnspan=1)

        self.warning_label = Label(text="", bg="#fff", fg="#222831")
        self.warning_label.grid(column=0, row=4, columnspan=1)

        self.root.mainloop()

    def launch_control(self, file_path):
        if os.path.isfile(file_path):
            # Pass selected media to control vlc media player in control
            control = Control(file_path)
        else:
            self.warning_label.config(text="No media found. Please check the file path and try again")

    # Open file browser for selecting video
    def browsefiles(self):
        filename = filedialog.askopenfilename(title="Select file",
                                              filetypes=(("mp4 files","*.mp4"),
                                                           ("all files",
                                                            "*.*")))
        print(filename)
        self.launch_control(filename)
