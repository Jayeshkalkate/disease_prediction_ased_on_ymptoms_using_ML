import tkinter as tk
from tkinter import messagebox, PhotoImage, Toplevel
import PIL  # Placeholder for actual use, remove if unused

# Create a fullscreen toplevel window
root = Toplevel()
root.wm_attributes("-fullscreen", True)
root.configure(background='black')
root.title("Login Page")

# Exit confirmation
def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system?")
    if qExit:
        root.destroy()
        exit()

# Navigation functions
def usermodule():
    import login_form

def adminmodule():
    import admin_module

# Background image
bg_image = PhotoImage(file="C:\\newone\\Screenshot (22).png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=100, y=150)

# User icon
user_icon  = PhotoImage(file="C:\\newone\\profile.png")
user_label = tk.Label(root, image=user_icon)
user_label.place(x=950, y=120)

# Admin icon
admin_icon  = PhotoImage(file="C:\\newone\\admin.png")
admin_label = tk.Label(root, image=admin_icon)
admin_label.place(x=950, y=400)

# User button
user_button = tk.Button(
    root,
    text="User",
    command=usermodule,
    bg="#FFA781",
    fg="#5B0E2D",
    width=10,
    font=("Times", 15, "bold")
)
user_button.place(x=970, y=300)

# Admin button
admin_button = tk.Button(
    root,
    text="Admin",
    command=adminmodule,
    bg="#FFD55A",
    fg="#293250",
    width=10,
    font=("Times", 15, "bold")
)
admin_button.place(x=970, y=580)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    command=Exit,
    bg="black",
    fg="sky blue",
    width=10,
    font=("Times", 15, "bold")
)
exit_button.place(x=1100, y=650)

# Start event loop
root.mainloop()
