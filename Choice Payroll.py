import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def search_employee():
    # Placeholder function for search employee functionality
    pass

window = tk.Tk()
window.title("Bianca's Choice Payroll")

# Load and resize the image
image = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\Default.jpg')
resized_image = image.resize((150, 150))
employee_image = ImageTk.PhotoImage(resized_image)

# Create frame for basic employee info
frame = Frame(window, padx=20, pady=20)
frame.grid(row=1, column=0)

# Bold text for employee basic info
Label(frame, text="EMPLOYEE BASIC INFO:", font=("Arial", 8, "bold")).grid(row=1, column=0, columnspan=2, padx=(0,40), pady=(0, 10))

# Labels and Entry Widgets for basic employee info
Label(frame, text="Firstname:").grid(row=1, column=2, sticky=E, padx=(150,10),pady=(30, 5))
Label(frame, text="Middle Name:").grid(row=2, column=2, sticky=E, pady=5)
Label(frame, text="Surname:").grid(row=3, column=2, sticky=E, pady=5)
Label(frame, text="Civil Status:").grid(row=4, column=2, sticky=E, pady=5)
Label(frame, text="Qualified Dependents Status:").grid(row=5, column=2, sticky=E, pady=5)
Label(frame, text="Paydate:").grid(row=6, column=2, sticky=E, pady=5)
Label(frame, text="Employee Status:").grid(row=7, column=2, sticky=E, pady=5)
Label(frame, text="Designation:").grid(row=8, column=2, sticky=E, pady=(5, 20))

# Entry widgets
Entry(frame).grid(row=1, column=3, pady=(30, 5))
Entry(frame).grid(row=2, column=3, pady=5)
Entry(frame).grid(row=3, column=3, pady=5)
Entry(frame).grid(row=4, column=3, pady=5)
Entry(frame).grid(row=5, column=3, pady=5)
Entry(frame).grid(row=6, column=3, pady=5)
Entry(frame).grid(row=7, column=3, pady=5)
Entry(frame).grid(row=8, column=3, pady=(5, 20))

# Labels and Entry Widgets for basic employee info
Label(frame, text="REGULAR DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=9, column=2, sticky=E, pady=5)
Label(frame, text="SSS Contribution:").grid(row=10, column=2, sticky=E, pady=5)
Label(frame, text="Philhealth Contribution:").grid(row=11, column=2, sticky=E, pady=5)
Label(frame, text="Pagibig Contribution:").grid(row=12, column=2, sticky=E, pady=5)
Label(frame, text="Income Tax Contribution:").grid(row=13, column=2, sticky=E, pady=5)

# Entry widgets
Entry(frame).grid(row=10, column=3, pady=5)
Entry(frame).grid(row=11, column=3, pady=5)
Entry(frame).grid(row=12, column=3, pady=5)
Entry(frame).grid(row=13, column=3, pady=5)

Label(frame, text="OTHER DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=14, column=2, sticky=E, pady=5)
Label(frame, text="SSS Loan:").grid(row=15, column=2, sticky=E, pady=5)
Label(frame, text="Pagibig Loan:").grid(row=16, column=2, sticky=E, pady=5)
Label(frame, text="Faculty Savings Deposit:").grid(row=17, column=2, sticky=E, pady=5)
Label(frame, text="Faculty Savings Loan:").grid(row=18, column=2, sticky=E, pady=5)
Label(frame, text="Salary Loan:").grid(row=19, column=2, sticky=E, pady=5)
Label(frame, text="Other Loan:").grid(row=20, column=2, sticky=E, pady=5)

# Entry widgets
Entry(frame).grid(row=15, column=3, pady=5)
Entry(frame).grid(row=16, column=3, pady=5)
Entry(frame).grid(row=17, column=3, pady=5)
Entry(frame).grid(row=18, column=3, pady=5)
Entry(frame).grid(row=19, column=3, pady=5)
Entry(frame).grid(row=20, column=3, pady=5)

Label(frame, text="DEDUCTION SUMMARY:", font=("Arial", 10, "bold")).grid(row=21, column=2, sticky=E, pady=5)
Label(frame, text="Total Deduction:").grid(row=22, column=2, sticky=E, pady=5)

Entry(frame).grid(row=21, column=3, pady=5)
Entry(frame).grid(row=22, column=3, pady=5)

# Gross Income Button
Button(frame, text="GROSS INCOME", command=search_employee, bg="sky blue").grid(row=23, column=2, padx=(30, 5), pady=5, sticky=W)

# NET INCOME Button
Button(frame, text="NET INCOME", command=search_employee, bg="sky blue").grid(row=23, column=2, padx=(130, 0), pady=5, sticky=W)

# SAVE Button
Button(frame, text="SAVE", command=search_employee, bg="light green").grid(row=23, column=3, padx=(0, 0), pady=5, sticky=W)

# Update Button
Button(frame, text="UPDATE", command=search_employee, bg="light green").grid(row=23, column=3, padx=(40,0), pady=5, sticky=W)

# New Button
Button(frame, text="NEW", command=search_employee, bg="light yellow").grid(row=23, column=3, padx=(100,0), pady=5, sticky=W)


# Add employee image with padding
Label(frame, image=employee_image).grid(row=1, column=0, rowspan=6, columnspan=2, padx=(0, 10), pady=(30, 0), sticky=N)

# Labels and Entry Widgets for employee number and department
Label(frame, text="Employee Number:").grid(row=6, column=0, sticky=E, pady=(20, 5))
Label(frame, text="Department:").grid(row=8, column=0, sticky=E, pady=5)

Entry(frame).grid(row=6, column=1, padx=(0,50), pady=(20, 5))
Entry(frame).grid(row=8, column=1, padx=(0,50), pady=5)

# Search Button and Label
Label(frame, text="Search Employee:").grid(row=7, column=0, padx=(30, 5), pady=5, sticky=E)
Button(frame, text="Search", command=search_employee, bg="Red").grid(row=7, column=1, padx=(0, 50), pady=5, sticky=W)

# Basic Income Section
Label(frame, text="BASIC INCOME:", font=("Arial", 10, "bold")).grid(row=9, column=0, sticky=E, pady=5)
Label(frame, text="Rate/ Hour:").grid(row=10, column=0, sticky=E, pady=5)
Label(frame, text="No of Hours/ Cut off:").grid(row=11, column=0, sticky=E, pady=5)
Label(frame, text="Income/ Cut off:").grid(row=12, column=0, sticky=E, pady=5)

Entry(frame).grid(row=10, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=11, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=12, column=1, padx=(0,50), pady=5)

# Honorarium Section
Label(frame, text="HONORARIUM INCOME:", font=("Arial", 10, "bold")).grid(row=13, column=0, sticky=E, pady=5)
Label(frame, text="Rate/ Hour:").grid(row=14, column=0, sticky=E, pady=5)
Label(frame, text="No of Hours/ Cut off:").grid(row=15, column=0, sticky=E, pady=5)
Label(frame, text="Income/ Cut off:").grid(row=16, column=0, sticky=E, pady=5)

Entry(frame).grid(row=14, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=15, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=16, column=1, padx=(0,50), pady=5)

# Other Income Section
Label(frame, text="OTHER INCOME:", font=("Arial", 10, "bold")).grid(row=17, column=0, sticky=E, pady=5)
Label(frame, text="Rate/ Hour:").grid(row=18, column=0, sticky=E, pady=5)
Label(frame, text="No of Hours/ Cut off:").grid(row=19, column=0, sticky=E, pady=5)
Label(frame, text="Income/ Cut off:").grid(row=20, column=0, sticky=E, pady=5)

Entry(frame).grid(row=18, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=19, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=20, column=1, padx=(0,50), pady=5)

# Summary Section
Label(frame, text="SUMMARY INCOME:", font=("Arial", 10, "bold")).grid(row=21, column=0, sticky=E, pady=5)
Label(frame, text="GROSS INCOME:").grid(row=22, column=0, sticky=E, pady=5)
Label(frame, text="NET INCOME:").grid(row=23, column=0, sticky=E, pady=5)

Entry(frame).grid(row=22, column=1, padx=(0,50), pady=5)
Entry(frame).grid(row=23, column=1, padx=(0,50), pady=5)

# Labels and Entry Widgets for payroll info
Label(window, text="Bianca's Choice Payroll", font=("Times New Roman", 30, "bold")).grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")


window.mainloop()