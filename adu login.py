from tkinter import Label, CENTER

import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x700")
app.title("Final Project")


# Function to handle login logic
def login():
    username = "123"
    password = "123"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong Password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong Username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and Password")


# Function to handle sign-up (dummy function)
def sign_up():
    tkmb.showinfo(title="Sign Up", message="Sign Up Functionality to be implemented")


# Set up the background image
image = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\background.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((900, 700)))
background_label = Label(app, image=bck_pic)
background_label.place(x=0, y=0)

# Create frame for login section
frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label = ctk.CTkLabel(master=frame, text='Login Page', font=('Helvetica', 20, 'bold'))
label.pack(pady=20)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=200)
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=200)
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login, width=200)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

# Sign Up section
sign_up_text = ctk.CTkLabel(master=frame, text="Not registered?", font=('Helvetica', 10))
sign_up_text.pack(pady=(20, 5))

sign_up_button = ctk.CTkButton(master=frame, text='Sign Up', command=sign_up, width=200, fg_color='transparent',
                               text_color='#57a1f8')
sign_up_button.pack(pady=(0, 10))

app.mainloop()

