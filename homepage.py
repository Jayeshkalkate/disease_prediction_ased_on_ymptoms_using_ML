import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import os

# Initialize root window
root = tk.Tk()
root.minsize(800, 800)
root.title("Disease Prediction Based on Symptoms using Machine Learning")
root.configure(background='black')
root.wm_attributes("-fullscreen", True)

# Exit confirmation
def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system?")
    if qExit:
        root.destroy()
        exit()

# Login page redirection
def login():
    import login_page

# Background image
background_img = PhotoImage(file="C:\\newone\\Screenshot (21).png")
background_label = tk.Label(root, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title_label = tk.Label(
    root,
    text="Disease Prediction Based on Symptoms using Machine Learning",
    fg="darkgreen",
    bg="white",
    font=("Times", 26, "bold"),
    justify="center"
)
title_label.place(x=175, y=50)

# About Section
about_title = tk.Label(root, text="About Us !!!", fg="purple", bg="white", font=("Times", 22, "bold"))
about_title.place(x=100, y=150)

about_lines = [
    "The general day-to-day health of a person is vital for efficient functioning of the human body.",
    "Taking certain symptoms and their disease, we build a machine learning model to predict diseases.",
    "The proposed model uses different machine learning algorithms to achieve accurate prediction."
]

y_pos = 200
for line in about_lines:
    label = tk.Label(root, text=line, fg="black", bg="white", font=("Times", 19, "bold"), justify="left")
    label.place(x=100, y=y_pos)
    y_pos += 35

# Buttons
start_button = tk.Button(
    root,
    text="Get Started",
    command=login,
    fg="white",
    bg="green",
    font=("Times", 22, "bold")
)
start_button.place(x=100, y=340)

exit_button = tk.Button(
    root,
    text="Exit",
    command=Exit,
    fg="sky blue",
    bg="black",
    font=("Times", 15, "bold"),
    width=10
)
exit_button.place(x=1100, y=650)

# Mainloop
root.mainloop()
