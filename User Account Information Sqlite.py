import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def update_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE user_account_info
            SET first_name = ?, middle_name = ?, last_name = ?, suffix = ?, department = ?, 
                designation = ?, username = ?, password = ?, confirm_password = ?, user_type = ?, 
                user_status = ?
            WHERE employee_number = ?
        ''', (
            FirstName.get(), MiddleName.get(), LastName.get(), Suffix.get(), Department.get(),
            Designation.get(), Username.get(), Password.get(), ConfirmPassword.get(), UserType.get(),
            UserStatus.get(), EmployeeNumber.get()
        ))

        conn.commit()
        conn.close()
        print("User data has been successfully updated.")

    except Exception as e:
        print("Error updating user data:", e)


def delete_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM user_account_info WHERE employee_number = ?
        ''', (EmployeeNumber.get(),))

        conn.commit()
        conn.close()
        print("User data has been successfully deleted.")

        # Clear all entry fields
        clear_fields()

    except Exception as e:
        print("Error deleting user data:", e)


def cancel_operation():
    window.destroy()


def clear_fields():
    FirstName.delete(0, END)
    MiddleName.delete(0, END)
    LastName.delete(0, END)
    Suffix.delete(0, END)
    Department.delete(0, END)
    Designation.delete(0, END)
    Username.delete(0, END)
    Password.delete(0, END)
    ConfirmPassword.delete(0, END)
    UserType.delete(0, END)
    UserStatus.delete(0, END)
    EmployeeNumber.delete(0, END)


def insert_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO user_account_info (
                first_name, middle_name, last_name, suffix, department, designation, 
                username, password, confirm_password, user_type, user_status, employee_number
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            FirstName.get(), MiddleName.get(), LastName.get(), Suffix.get(), Department.get(),
            Designation.get(), Username.get(), Password.get(), ConfirmPassword.get(), UserType.get(),
            UserStatus.get(), EmployeeNumber.get()
        ))

        conn.commit()
        conn.close()
        print("User data has been successfully inserted.")

        # Clear all entry fields
        clear_fields()

    except Exception as e:
        print("Error inserting user data:", e)


# Create the GUI
window = tk.Tk()
window.title("User Account Information")

# Create frame with .place() and set it to be behind other widgets
frame = tk.Frame(window, width=890, height=370, bg='dark grey')
frame.place(x=20, y=70)
frame.lower()

# Load and resize the image
image1 = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\default3.jpg')
resized_image = image1.resize((100, 100))
employee_image = ImageTk.PhotoImage(resized_image)

# Create frame for user account info using .place()
user_frame = tk.Frame(window, padx=20, pady=20)
user_frame.place(x=37, y=80)

heading = Label(text="User Account Information", fg='black', font=('Times New Roman', 15,))
heading.place(x=37, y=105, width=500)
heading.config(fg='black')

# Add user image with padding
Label(user_frame, image=employee_image).grid(row=0, column=0, rowspan=3, padx=(20, 10), pady=(40, 10), sticky=W)

# Labels and Entry Widgets for user account info
Label(user_frame, text="First Name:").grid(row=1, column=1, rowspan=2, sticky=W, pady=(5, 0))
FirstName = Entry(user_frame)
FirstName.grid(row=2, column=1, pady=5, padx=5)

Label(user_frame, text="Middle Name:").grid(row=1, column=2, rowspan=2, sticky=W, pady=(5, 0))
MiddleName = Entry(user_frame)
MiddleName.grid(row=2, column=2, pady=5, padx=5)

Label(user_frame, text="Last Name:").grid(row=1, column=3, rowspan=2, sticky=W, pady=(5, 0))
LastName = Entry(user_frame)
LastName.grid(row=2, column=3, pady=5, padx=5)

Label(user_frame, text="Suffix:").grid(row=1, column=4, rowspan=2, sticky=W, pady=(5, 0))
Suffix = Entry(user_frame)
Suffix.grid(row=2, column=4, pady=5, padx=5)

Label(user_frame, text="Department:").grid(row=1, column=5, rowspan=2, sticky=W, pady=(5, 0))
Department = Entry(user_frame)
Department.grid(row=2, column=5, pady=5, padx=5)

# Labels and Entry Widgets for user login info
Label(user_frame, text="Designation:").place(x=5, y=155)
Designation = Entry(user_frame)
Designation.place(x=5, y=175, width=280)

Label(user_frame, text="Username:").place(x=285, y=155)
Username = Entry(user_frame)
Username.place(x=290, y=175, width=240)

Label(user_frame, text="Password:").place(x=540, y=155)
Password = Entry(user_frame, show="*")
Password.grid(row=4, column=4, padx=0, pady=20, columnspan=2)

Label(user_frame, text="Confirm Password:").place(x=5, y=225)
ConfirmPassword = Entry(user_frame, show="*")
ConfirmPassword.grid(row=6, column=0, pady=5, columnspan=2)

Label(user_frame, text="User Type:").place(x=285, y=225)
UserType = Entry(user_frame)
UserType.place(x=285, y=250, width=240)

Label(user_frame, text="User Status:").place(x=540, y=225)
UserStatus = Entry(user_frame)
UserStatus.place(x=535, y=250, width=140)

Label(user_frame, text="Employee Number:").grid(row=5, column=5, sticky=W, pady=(10, 0))
EmployeeNumber = Entry(user_frame)
EmployeeNumber.place(x=680, y=250, width=140)

# Buttons for user account actions
Button(user_frame, text="Update", bg="light blue", command=update_user).place(x=130, y=280, width=80)
Button(user_frame, text="Delete", bg="light yellow", command=delete_user).place(x=220, y=280, width=80)
Button(user_frame, text="Cancel", bg="white", width=10, command=cancel_operation).grid(row=7, column=2, padx=(20, 5),
                                                                                       pady=5)

# Button to insert user
Button(user_frame, text="Insert", bg="light green", command=insert_user).place(x=40, y=280, width=80)

# Connect to the same SQLite database and create table for user account info if not exists
conn = sqlite3.connect('EmployeeDatabase2.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_account_info (
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    suffix TEXT,
    department TEXT,
    designation TEXT,
    username TEXT,
    password TEXT,
    confirm_password TEXT,
    user_type TEXT,
    user_status TEXT,
    employee_number TEXT PRIMARY KEY
)
''')
conn.commit()
conn.close()

window.geometry('935x460')
window.mainloop()

