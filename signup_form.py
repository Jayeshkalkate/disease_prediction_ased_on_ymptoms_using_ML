import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar, IntVar, Toplevel
import sqlite3

# Create the signup window
root = Toplevel()
root.geometry('500x500')
root.title("Registration Form")
root.configure(background='white')

# Variables for form inputs
name = StringVar()
email = StringVar()
password = StringVar()
age = StringVar()
gender = IntVar()  # 1 for Male, 2 for Female

# Navigate to login form
def login():
    import login_form

# Function to insert data into the database
def database_s():
    name_val = name.get().strip()
    email_val = email.get().strip()
    password_val = password.get().strip()
    age_val = age.get().strip()
    gender_val = gender.get()

    gender_text = "Male" if gender_val == 1 else "Female" if gender_val == 2 else ""

    if not all([name_val, email_val, password_val, age_val, gender_text]):
        lbl_text.config(text="Please complete all required fields!", fg="red")
        return

    if not age_val.isdigit():
        lbl_text.config(text="Age must be an integer", fg="red")
        return

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PatientDetails (
                Name TEXT,
                Email TEXT,
                Password TEXT,
                Age INTEGER,
                Gender TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO PatientDetails (Name, Email, Password, Age, Gender)
            VALUES (?, ?, ?, ?, ?)
        ''', (name_val, email_val, password_val, int(age_val), gender_text))
        conn.commit()
        lbl_text.config(text="Sign Up Successful", fg="green")
        login()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cursor.close()
        conn.close()

# Background image
bg = PhotoImage(file="C:\\newone\\Screenshot (24).png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=50, y=0)
bg_label.image = bg

# Form Labels and Entries
tk.Label(root, text="Name", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=130)
tk.Entry(root, textvariable=name, width=30).place(x=240, y=130)

tk.Label(root, text="Email", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=180)
tk.Entry(root, textvariable=email, width=30).place(x=240, y=180)

tk.Label(root, text="Password", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=230)
tk.Entry(root, textvariable=password, show="*", width=30).place(x=240, y=230)

tk.Label(root, text="Age", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=280)
tk.Entry(root, textvariable=age, width=30).place(x=240, y=280)

tk.Label(root, text="Gender", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=330)
tk.Radiobutton(root, text="Male", variable=gender, value=1).place(x=235, y=330)
tk.Radiobutton(root, text="Female", variable=gender, value=2).place(x=310, y=330)

# Submit and Login buttons
tk.Button(root, text='SUBMIT', width=15, font=("bold", 10), bg='#143D59', fg='#F4B41A', command=database_s).place(x=180, y=400)
tk.Button(root, text='LOGIN', width=15, font=("bold", 10), bg='#143D59', fg='#F4B41A', command=login).place(x=180, y=450)

# Feedback Label
Form = tk.Frame(root, height=200)
Form.pack(side=tk.TOP, pady=20)
lbl_text = tk.Label(Form, text="")
lbl_text.grid(row=2, columnspan=2)

# Start the window
root.mainloop()
