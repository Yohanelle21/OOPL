import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def search_employee():
    # Placeholder function for search employee functionality
    pass

def choose_image():
    # Placeholder function for choosing an image
    pass

window = tk.Tk()
window.title("Combined Application")

# Function to load and resize image
def load_image(file_path, size):
    image = Image.open(file_path)
    resized_image = image.resize(size)
    return ImageTk.PhotoImage(resized_image)

# Load and resize the image for employee
employee_image = load_image('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\Default.jpg', (150, 150))

# Load and resize the image for user account
user_image = load_image('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\default3.jpg', (100, 100))

# Frame for image selection
image_frame = Frame(window, padx=20, pady=20)
image_frame.grid(row=0, column=0, sticky="nsew")

# Add user image with padding and Choose File button
Label(image_frame, image=user_image).grid(row=0, column=0, rowspan=5, padx=(20, 10), pady=(40,10), sticky=W)
Button(image_frame, text="Choose File", command=choose_image).grid(row=5, column=0, padx=(20, 10), pady=(10,0), sticky=W)
Label(image_frame, text="No file chosen").place(x=100, y=165)

# Personal Information Section
personal_frame = Frame(window, padx=20, pady=20)
personal_frame.grid(row=0, column=1, sticky="nsew")

Label(personal_frame, text="PERSONAL INFORMATION", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

# Labels and Entry Widgets for personal information
personal_labels = ["First Name:", "Middle Name:", "Last Name:", "Suffix:", "Date of Birth:", "Gender:", "Nationality:", "Civil Status:"]
personal_entries = [Entry(personal_frame) for _ in range(len(personal_labels))]

for i, label in enumerate(personal_labels):
    Label(personal_frame, text=label).grid(row=1, column=i*2, padx=(5,0), pady=5, sticky=E)
    personal_entries[i].grid(row=1, column=i*2+1, padx=(0,5), pady=5, sticky=W)

# User Account Information Section
user_frame = Frame(window, padx=20, pady=20)
user_frame.grid(row=1, column=0, sticky="nsew")

Label(user_frame, text="USER ACCOUNT INFORMATION", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Widgets for user account information
user_labels = ["Designation:", "Username:", "Password:", "Confirm Password:", "User Type:", "User Status:", "Employee Number:"]
user_entries = [Entry(user_frame) for _ in range(len(user_labels))]

for i, label in enumerate(user_labels):
    Label(user_frame, text=label).grid(row=i, column=0, padx=(5,0), pady=5, sticky=E)
    user_entries[i].grid(row=i, column=1, padx=(0,5), pady=5, sticky=W)

# Buttons for user account actions
Button(user_frame, text="Update", bg="light blue").grid(row=len(user_labels)+1, column=0, padx=10, pady=10)
Button(user_frame, text="Delete", bg="light yellow").grid(row=len(user_labels)+1, column=1, padx=10, pady=10)
Button(user_frame, text="Cancel", bg="white", width=10).grid(row=len(user_labels)+1, column=2, padx=10, pady=10)

# Employee Details Section
employee_frame = Frame(window, padx=20, pady=20)
employee_frame.grid(row=1, column=1, sticky="nsew")

Label(employee_frame, text="EMPLOYEE DETAILS", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Widgets for employee details
employee_labels = ["Department:", "Designation:", "Qualified Dependents Status:", "Employee Status:", "Paydate:", "Employee Number:"]
employee_entries = [Entry(employee_frame) for _ in range(len(employee_labels))]

for i, label in enumerate(employee_labels):
    Label(employee_frame, text=label).grid(row=i, column=0, padx=(5,0), pady=5, sticky=E)
    employee_entries[i].grid(row=i, column=1, padx=(0,5), pady=5, sticky=W)

# Dropdown options for Gender
genders = ["Male", "Female", "Other"]
gender_var = StringVar()
gender_dropdown = OptionMenu(personal_frame, gender_var, *genders)
gender_var.set("Male")
gender_dropdown.grid(row=1, column=13, padx=(0,5), pady=5, sticky="ew")

# Dropdown options for Nationality
nationalities = ["Christian", "Muslim", "Hindu", "Buddhist", "Other"]
nationality_var = StringVar()
nationality_dropdown = OptionMenu(personal_frame, nationality_var, *nationalities)
nationality_var.set("Christian")
nationality_dropdown.grid(row=1, column=15, padx=(0,5), pady=5, sticky="ew")

# Dropdown options for Civil Status
civil_statuses = ["Single", "Married", "Divorced", "Widowed"]
civil_status_var = StringVar()
civil_status_dropdown = OptionMenu(personal_frame, civil_status_var, *civil_statuses)
civil_status_var.set("Single")
civil_status_dropdown.grid(row=1, column=17, padx=(0,5), pady=5, sticky="ew")

# Dropdown options for User Type
user_types = ["Admin", "User"]
user_type_var = StringVar()
user_type_dropdown = OptionMenu(user_frame, user_type_var, *user_types)
user_type_var.set("Admin")
user_type_dropdown.grid(row=len(user_labels)-1, column=1, padx=10, pady=5, sticky="ew")

# Dropdown options for User Status
user_statuses = ["Active", "Inactive"]
user_status_var = StringVar()
user_status_dropdown = OptionMenu(user_frame, user_status_var, *user_statuses)
user_status_var.set("Active")
user_status_dropdown.grid(row=len(user_labels), column=1, padx=10, pady=5, sticky="ew")

# Dropdown options for Qualified Dependents Status
qualified_statuses = ["Yes", "No"]
qualified_var = StringVar()
qualified_dropdown = OptionMenu(employee_frame, qualified_var, *qualified_statuses)
qualified_var.set("Yes")
qualified_dropdown.grid(row=2, column=1, padx=(0,5), pady=5, sticky="ew")

# Dropdown options for Employee Status
employee_statuses = ["Active", "Inactive"]
employee_status_var = StringVar()
employee_status_dropdown = OptionMenu(employee_frame, employee_status_var, *employee_statuses)
employee_status_var.set("Active")
employee_status_dropdown.grid(row=3, column=1, padx=(0,5), pady=5, sticky="ew")

# Entry for Paydate
paydate_var = StringVar()
paydate_entry = Entry(employee_frame, textvariable=paydate_var)
paydate_var.set("YYYY-MM-DD")
paydate_entry.grid(row=4, column=1, padx=(0,5), pady=5, sticky="ew")

# Start the main loop
window.mainloop()


