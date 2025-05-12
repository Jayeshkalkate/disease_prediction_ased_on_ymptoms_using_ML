import tkinter as tk
from tkinter import messagebox, PhotoImage
import sqlite3

# Create the feedback form window
root = tk.Toplevel()
root.geometry('900x900')
root.title("Feedback Form")

# Read email from file
with open('email.txt', 'r') as f:
    email = f.read().strip()

# Function to submit the feedback to the database
def database_s():
    name = Name.get()
    comments = Comments.get()

    if not name or not comments:
        lbl_text.config(text="Please complete the required fields!", fg="red")
        return

    # Connect to the database and save the feedback
    conn = sqlite3.connect('database.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Feedback (Id INTEGER PRIMARY KEY, Name TEXT, Comments TEXT)")
        cursor.execute("INSERT INTO Feedback (Name, Comments) VALUES (?, ?)", (name, comments))
        conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo(title="Feedback", message="Feedback Submitted!")

# Function to clear the form
def clear():
    Name.set("")
    Comments.set("")

# Function to exit the application
def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system?")
    if qExit:
        root.destroy()

# Fetch the user's name based on the email
conn2 = sqlite3.connect("database.db")
cur2 = conn2.cursor()
cur2.execute("SELECT Name FROM PatientDetails WHERE `Email` = ?", (email,))
name = cur2.fetchone()
cur2.close()
conn2.close()

# Set up the Tkinter variables
Name = tk.StringVar()
Name.set(name[0] if name else "")
Comments = tk.StringVar()

# Background image
bg = PhotoImage(file="C:\\newone\\Screenshot (26).png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=250, y=120)
bg_label.image = bg

# UI Elements
label_1 = tk.Label(root, text="Tell us what you think!", width=20, font=("bold", 17), fg='#e52165', bg='#0d1137')
label_1.place(x=320, y=50)

label_2 = tk.Label(root, text="Name", width=20, font=("bold", 13), fg='#5300C6')
label_2.place(x=150, y=330)
entry_1 = tk.Entry(root, textvariable=Name, state="disabled", width=53)
entry_1.place(x=340, y=330)

label_3 = tk.Label(root, text="Comments", width=20, font=("bold", 13), fg='#5300C6')
label_3.place(x=150, y=380)
entry_2 = tk.Entry(root, textvariable=Comments, width=53)
entry_2.place(x=340, y=380)

# Buttons
tk.Button(root, text='SUBMIT', width=20, font=("bold", 12), bg='#F9868B', fg='#761137', command=database_s).place(x=395, y=470)
tk.Button(root, text='CLEAR', width=20, font=("bold", 12), bg='#F9868B', fg='#761137', command=clear).place(x=395, y=520)
tk.Button(root, text='Exit', bg="Black", fg="SkyBlue", font=("Times", 15, "bold"), width=10, command=Exit).place(x=1120, y=605)

# Feedback message label
Form = tk.Frame(root, height=200)
Form.pack(side=tk.TOP, pady=20)
lbl_text = tk.Label(Form)
lbl_text.grid(row=2, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
