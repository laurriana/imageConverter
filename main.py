import tkinter
import customtkinter
from tkinter import filedialog as fd
from tkinter import Frame

# module imports
from converter import webpToPng, pngToIco

# system settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

title = "Confirmation"
message = "All files converted successfully :)"

# app frame
app = customtkinter.CTk()
app.geometry("520x120")
app.title("image converter")
app.resizable(False, False)

# set the window icon
try:
    with open("icon", "r") as file:
        icon = file.read()
    app.iconbitmap(icon)
except FileNotFoundError:
    pass # ignore if file not found

# title
title = customtkinter.CTkLabel(app, text="Import your files", font=("TkDefaultFont", 16))
title.pack(padx=10, pady=10)

# webP to png button
def open_file_dialog_webPtoPng():
    global fileLinks
    fileLinks = fd.askopenfilenames(filetypes=[("WebP images", "*.webp")])
    for fileLink in fileLinks:
        webpToPng(fileLink)
    tkinter.messagebox.showinfo(title=title, message=message)

# png to ico button
def open_file_dialog_pngToIco():
    global fileLinks
    fileLinks = fd.askopenfilenames(filetypes=[("Png images", "*.png")])
    for fileLink in fileLinks:
        pngToIco(fileLink)
    tkinter.messagebox.showinfo(title=title, message=message)

# change app icon button
def change_app_icon():
    icon = fd.askopenfilename(filetypes=[("Icon", "*.ico")])
    
    # save icon path to file
    with open("icon", "w") as file:
        file.write(icon)

    app.iconbitmap(icon)

button_frame = Frame(app, bg=app.cget('bg'))
button_frame.pack()

# webP to png button
button1 = customtkinter.CTkButton(button_frame, text="webP to Png", command=open_file_dialog_webPtoPng)
button1.grid(row=0, column=0, padx=10, pady=10)

# png to ico button
button2 = customtkinter.CTkButton(button_frame, text="png to ico", command=open_file_dialog_pngToIco)
button2.grid(row=0, column=1, padx=10, pady=10)

# change app icon button
button3 = customtkinter.CTkButton(button_frame, text="change app icon", command=change_app_icon)
button3.grid(row=0, column=2, padx=10, pady=10)

# run app
app.mainloop()