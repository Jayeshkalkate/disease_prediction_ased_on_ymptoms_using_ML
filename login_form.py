import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar, Toplevel
import sqlite3

# Create the login window
root = Toplevel()
root.geometry('500x500')
root.title("Login Form")
root.configure(background='white')

# Variables for input fields
email = StringVar()
password = StringVar()

# Handle login verification
def database():
    email_input = email.get().strip()
    password_input = password.get().strip()

    if email_input == "" or password_input == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        return

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM PatientDetails WHERE Email = ? AND Password = ?",
            (email_input, password_input)
        )
        if cursor.fetchone():
            lbl_text.config(text="Login Successful", fg="green")
            email.set("")
            password.set("")

            with open('email.txt', 'w') as f:
                f.write(email_input)

            import user_module
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            email.set("")
            password.set("")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cursor.close()
        conn.close()

# Handle navigation to sign-up form
def sign_up():
    import sign_up_form

# Set background image
bg = PhotoImage(file="C:\\newone\\Screenshot (23).png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0)
bg_label.image = bg  # Keep reference

# Email label and entry
tk.Label(root, text="Email", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=130)
tk.Entry(root, textvariable=email, width=30).place(x=260, y=130)

# Password label and entry
tk.Label(root, text="Password", width=20, font=("bold", 11), fg='#5300C6').place(x=80, y=180)
tk.Entry(root, textvariable=password, show="*", width=30).place(x=260, y=180)

# Login button
tk.Button(
    root,
    text='LOGIN',
    width=20,
    font=("bold", 10),
    bg='#143D59',
    fg='#F4B41A',
    command=database
).place(x=195, y=250)

# Signup button
tk.Button(
    root,
    text='NEW USER > SIGN UP',
    width=20,
    font=("bold", 10),
    bg='#143D59',
    fg='#F4B41A',
    command=sign_up
).place(x=195, y=330)

# Message label
Form = tk.Frame(root, height=200)
Form.pack(side=tk.TOP, pady=20)
lbl_text = tk.Label(Form, text="")
lbl_text.grid(row=2, columnspan=2)

# Start the main event loop
root.mainloop()
