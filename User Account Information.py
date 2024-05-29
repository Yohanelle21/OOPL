import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def search_employee():
    # Placeholder function for search employee functionality
    pass

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
Label(user_frame, image=employee_image).grid(row=0, column=0, rowspan=3, padx=(20, 10), pady=(40,10), sticky=W)


# Labels and Entry Widgets for user account info
Label(user_frame, text="First Name:").grid(row=1, column=1, rowspan=2, sticky=W, pady=(5, 0))
Entry(user_frame).grid(row=2, column=1, pady=5, padx=5)
Label(user_frame, text="Middle Name:").grid(row=1, column=2, rowspan=2,sticky=W, pady=(5, 0))
Entry(user_frame).grid(row=2, column=2, pady=5, padx=5)
Label(user_frame, text="Last Name:").grid(row=1, column=3, rowspan=2,sticky=W, pady=(5, 0))
Entry(user_frame).grid(row=2, column=3, pady=5, padx=5)
Label(user_frame, text="Suffix:").grid(row=1, column=4, rowspan=2,sticky=W, pady=(5, 0))
Entry(user_frame).grid(row=2, column=4, pady=5, padx=5)
Label(user_frame, text="Department:").grid(row=1, column=5, rowspan=2,sticky=W, pady=(5, 0))
Entry(user_frame).grid(row=2, column=5, pady=5, padx=5)

# Labels and Entry Widgets for user login info
Label(user_frame, text="Designation:").place(x=5, y=155)
Entry(user_frame).place(x=5, y=175, width=280)
Label(user_frame, text="Username:").place(x=285, y=155)
Entry(user_frame).place(x=290, y=175, width=240)
Label(user_frame, text="Password:").place(x=540, y=155)
Entry(user_frame, show="*", width=45).grid(row=4, column=4, padx=0, pady=20,columnspan=2)
Label(user_frame, text="Confirm Password:").place(x=5, y=225)
Entry(user_frame, show="*", width=45).grid(row=6 , column=0, pady=5, columnspan=2)
Label(user_frame, text="User Type:").place(x=285, y=225)
Entry(user_frame).place(x=285, y=250, width=240)
Label(user_frame, text="User Status:").place(x=540, y=225)
Entry(user_frame).place(x=535,y=250, width=140)
Label(user_frame, text="Employee Number:").grid(row=5, column=5, sticky=W, pady=(10, 0))
Entry(user_frame).place(x=680, y=250, width=140)


# Buttons for user account actions
Button(user_frame, text="Update", bg="light blue").place(x=130, y=280, width=80)
Button(user_frame, text="Delete", bg="light yellow").place(x=220, y=280, width=80)
Button(user_frame, text="Cancel", bg="white", width=10).grid(row=7, column=2, padx=(20, 5), pady=5)


window.geometry('935x460')
window.mainloop()
