import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Fetch email from file
with open('email.txt', 'r') as f:
    email = f.read().strip()

# Function to handle the treeview clearing and updating
def update_treeview(query, params):
    tree.delete(*tree.get_children())  # Clear existing treeview data
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)  # Insert rows into the treeview
    con.close()

# Functions to fetch and display data for different models
def dec():
    query = "SELECT * FROM DecisionTree WHERE `Email` = ?"
    update_treeview(query, (email,))

def naive():
    query = "SELECT * FROM NaiveBayes WHERE `Email` = ?"
    update_treeview(query, (email,))

def knn():
    query = "SELECT * FROM KNearestNeighbour WHERE `Email` = ?"
    update_treeview(query, (email,))

def random():
    query = "SELECT * FROM RandomForest WHERE `Email` = ?"
    update_treeview(query, (email,))

# Function to handle exit confirmation
def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system?")
    if qExit:
        root.destroy()

# Placeholder function for feedback
def feedback():
    import feedback  # Assuming this is a separate module for feedback

# Tkinter setup
root = tk.Tk()
root.geometry("1290x800")
root.title("History")

# Treeview styling
style = ttk.Style()
style.configure("Treeview.Heading", font=("Times", 15, "bold"))

# Treeview widget to display data
tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show='headings')
tree.column("#1", minwidth=0, width=100, stretch="NO")
tree.heading("#1", text="Name")
tree.column("#2", minwidth=0, width=100, stretch="NO")
tree.heading("#2", text="Age")
tree.column("#3", minwidth=0, width=150, stretch="NO")
tree.heading("#3", text="Email")
tree.column("#4", minwidth=0, width=150, stretch="NO")
tree.heading("#4", text="s1")
tree.column("#5", minwidth=0, width=150, stretch="NO")
tree.heading("#5", text="s2")
tree.column("#6", minwidth=0, width=150, stretch="NO")
tree.heading("#6", text="s3")
tree.column("#7", minwidth=0, width=150, stretch="NO")
tree.heading("#7", text="s4")
tree.column("#8", minwidth=0, width=150, stretch="NO")
tree.heading("#8", text="s5")
tree.column("#9", minwidth=0, width=200, stretch="NO")
tree.heading("#9", text="Disease")
tree.pack()

# Buttons to trigger actions
tk.Button(root, text='DecisionTree', width=20, bg='brown', fg='white', command=dec).place(x=550, y=400)
tk.Button(root, text='NaiveBayes', width=20, bg='brown', fg='white', command=naive).place(x=550, y=450)
tk.Button(root, text='RandomForest', width=20, bg='brown', fg='white', command=random).place(x=550, y=500)
tk.Button(root, text='KNN', width=20, bg='brown', fg='white', command=knn).place(x=550, y=550)
tk.Button(root, text='Feedback', bg="Black", fg="Blue", font=("Times", 15, "bold"), width=10, command=feedback).place(x=1120, y=555)
tk.Button(root, text='Exit', bg="Black", fg="Blue", font=("Times", 15, "bold"), width=10, command=Exit).place(x=1120, y=605)

# Run the Tkinter event loop
root.mainloop()
