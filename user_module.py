import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Create fullscreen window
root = Toplevel()
root.title("User Module")
root.wm_attributes("-fullscreen", True)

# Exit function
def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system?")
    if qExit:
        root.destroy()
        exit()

# Navigation functions
def check_disease():
    import PythonCodeOfAlgorithm

def show_history():
    import history

def give_feedback():
    import feedback

# Background image
bg = PhotoImage(file="C:\\newone\\Screenshot (25).png")
bg_label = Label(root, image=bg)
bg_label.place(x=100, y=50)
bg_label.image = bg

# Buttons
Button(root, text="Check Disease", command=check_disease, bg="#FFA781", fg="#5B0E2D", width=20, font=("Times", 15, "bold")).place(x=1000, y=200)
Button(root, text="History", command=show_history, bg="#FFD55A", fg="#293250", width=20, font=("Times", 15, "bold")).place(x=1000, y=300)
Button(root, text="Feedback", command=give_feedback, bg="#00E1D9", fg="#5E001F", width=20, font=("Times", 15, "bold")).place(x=1000, y=400)
Button(root, text="Exit", command=Exit, bg="Black", fg="sky blue", width=10, font=("Times", 15, "bold")).place(x=1100, y=650)

# Run the user interface
root.mainloop()
