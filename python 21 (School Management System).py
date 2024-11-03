import tkinter as tk
from tkinter import messagebox, ttk

# Create the main window
root = tk.Tk()
root.title("School Management System")
root.geometry("600x400")

# List to store student data
students = []

# Function to add student
def add_student():
    name = entry_name.get()
    student_class = entry_class.get()
    roll_no = entry_roll.get()
    age = entry_age.get()

    if name and student_class and roll_no and age:
        # Check if roll number already exists
        for student in students:
            if student['Roll No'] == roll_no:
                messagebox.showwarning("Duplicate Roll No", "Roll No already exists!")
                return

        students.append({"Name": name, "Class": student_class, "Roll No": roll_no, "Age": age})
        update_student_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Function to clear the entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Function to update the student list display
def update_student_list():
    student_list.delete(*student_list.get_children())
    for idx, student in enumerate(students):
        student_list.insert("", "end", values=(student["Name"], student["Class"], student["Roll No"], student["Age"]))

# Function to edit selected student
def edit_student():
    selected_item = student_list.selection()
    if selected_item:
        item = student_list.item(selected_item)['values']
        roll_no = item[2]  # Use Roll No to identify the student
        
        # Find the student by Roll No and update details
        for student in students:
            if student["Roll No"] == roll_no:
                student["Name"] = entry_name.get()
                student["Class"] = entry_class.get()
                student["Age"] = entry_age.get()

        update_student_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Please select a student to edit.")

# Function to load selected student data into the entry fields
def load_student():
    selected_item = student_list.selection()
    if selected_item:
        item = student_list.item(selected_item)['values']
        roll_no = item[2]  # Use Roll No to identify the student

        # Load data into entry fields based on Roll No
        for student in students:
            if student["Roll No"] == roll_no:
                entry_name.delete(0, tk.END)
                entry_name.insert(tk.END, student["Name"])
                entry_class.delete(0, tk.END)
                entry_class.insert(tk.END, student["Class"])
                entry_roll.delete(0, tk.END)
                entry_roll.insert(tk.END, student["Roll No"])
                entry_age.delete(0, tk.END)
                entry_age.insert(tk.END, student["Age"])
    else:
        messagebox.showwarning("Selection Error", "Please select a student to load.")

# GUI layout
frame = tk.Frame(root)
frame.pack(pady=20)

label_name = tk.Label(frame, text="Name")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=10)

label_class = tk.Label(frame, text="Class")
label_class.grid(row=1, column=0)
entry_class = tk.Entry(frame)
entry_class.grid(row=1, column=1, padx=10)

label_roll = tk.Label(frame, text="Roll No")
label_roll.grid(row=2, column=0)
entry_roll = tk.Entry(frame)
entry_roll.grid(row=2, column=1, padx=10)

label_age = tk.Label(frame, text="Age")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(frame)
entry_age.grid(row=3, column=1, padx=10)

add_button = tk.Button(frame, text="Add Student", command=add_student)
add_button.grid(row=4, column=0, pady=10)

edit_button = tk.Button(frame, text="Edit Student", command=edit_student)
edit_button.grid(row=4, column=1, pady=10)

load_button = tk.Button(frame, text="Load Student", command=load_student)
load_button.grid(row=4, column=2, pady=10)

# Treeview for displaying student list
columns = ("Name", "Class", "Roll No", "Age")
student_list = ttk.Treeview(root, columns=columns, show="headings")
student_list.heading("Name", text="Name")
student_list.heading("Class", text="Class")
student_list.heading("Roll No", text="Roll No")
student_list.heading("Age", text="Age")
student_list.pack(pady=20)

root.mainloop()
