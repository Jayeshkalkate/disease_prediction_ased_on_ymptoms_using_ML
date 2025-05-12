import tkinter as tk
from tkinter import messagebox, StringVar
import sqlite3
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Global Variables
pred1 = StringVar()
pred2 = StringVar()
pred3 = StringVar()
pred4 = StringVar()

Symptom1 = StringVar(value="Select Here")
Symptom2 = StringVar(value="Select Here")
Symptom3 = StringVar(value="Select Here")
Symptom4 = StringVar(value="Select Here")
Symptom5 = StringVar(value="Select Here")

# Fetch patient details
with open("email.txt") as f:
    email = f.read()

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT Name, Age FROM PatientDetails WHERE Email = ?", (email,))
result = cur.fetchone()
conn.close()

Name = StringVar(value=result[0] if result else "")
Age = StringVar(value=result[1] if result else "")
Email = StringVar(value=email)

# Mock variables (replace with actual data)
X, y, X_test, y_test = [], [], [], []  # Replace with your dataset
l1 = ["Symptom1", "Symptom2", "Symptom3"]  # Example symptom list
l2 = [0] * len(l1)
disease = ["Disease1", "Disease2", "Disease3"]

def validate_input():
    if not Name.get():
        messagebox.showwarning("Validation", "Please fill in your name.")
        return False
    if Symptom1.get() == "Select Here" or Symptom2.get() == "Select Here":
        messagebox.showwarning("Validation", "Please select at least two symptoms.")
        return False
    return True

def process_symptoms():
    global l2
    l2 = [1 if sym in [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()] else 0 for sym in l1]
    return [l2]

def save_prediction(model_name, prediction):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {model_name}(
                Name TEXT, Age INTEGER, Email TEXT,
                Symptom1 TEXT, Symptom2 TEXT, Symptom3 TEXT,
                Symptom4 TEXT, Symptom5 TEXT, Disease TEXT
            )
        """)
        cursor.execute(f"""
            INSERT INTO {model_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (Name.get(), Age.get(), Email.get(),
              Symptom1.get(), Symptom2.get(), Symptom3.get(),
              Symptom4.get(), Symptom5.get(), prediction))

def predict_with_model(model, pred_var, model_name):
    if not validate_input():
        return

    model.fit(X, y)
    input_data = process_symptoms()
    prediction = model.predict(input_data)[0]

    pred_var.set(disease[prediction] if prediction < len(disease) else "Not Found")
    save_prediction(model_name, pred_var.get())

def DecisionTree():
    predict_with_model(tree.DecisionTreeClassifier(), pred1, "DecisionTree")

def randomforest():
    predict_with_model(RandomForestClassifier(n_estimators=100), pred2, "RandomForest")

def KNN():
    predict_with_model(KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2), pred4, "KNearestNeighbour")

def NaiveBayes():
    model = GaussianNB()
    model.fit(X, y)
    input_data = process_symptoms()
    prediction = model.predict(input_data)[0]

    pred3.set(disease[prediction] if prediction < len(disease) else "Not Found")
    save_prediction("NaiveBayes", pred3.get())

def Reset():
    for var in [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, pred1, pred2, pred3, pred4]:
        var.set("Select Here" if "Symptom" in var._name else "")

def Exit():
    if messagebox.askyesno("System", "Do you want to exit the system?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.configure(background='Black')
root.title('Disease Prediction Based on Symptoms using Machine Learning')
root.wm_attributes("-fullscreen", True)
