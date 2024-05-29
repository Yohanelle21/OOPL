import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def calculate_gross_income():
    try:
        # Basic Income calculation
        basic_rate_per_hour = float(basic_rate_hour.get())
        basic_no_of_hours = float(basic_no_of_hours_cutoff.get())
        basic_income_compute = float(basic_income_compute_both.get())
        basic_income = basic_rate_per_hour * basic_no_of_hours / basic_income_compute
        basic_income_var.set(basic_income)

        # Honorarium Income calculation
        honorarium_rate_per_hour = float(honorarium_rate_hour.get())
        honorarium_no_of_hours = float(honorarium_no_of_hours_cutoff.get())
        honorarium_income_compute = float(honorarium_income_compute_both.get())
        honorarium_income = honorarium_rate_per_hour * honorarium_no_of_hours / honorarium_income_compute
        honorarium_income_var.set(honorarium_income)

        # Other Income calculation
        other_rate_per_hour = float(other_rate_hour.get())
        other_no_of_hours = float(other_no_of_hours_cutoff.get())
        other_income_compute = float(other_income_compute_both.get())
        other_income = other_rate_per_hour * other_no_of_hours / other_income_compute
        other_income_var.set(other_income)

        # Gross Income calculation
        gross_income = basic_income + honorarium_income + other_income
        gross_income_var.set(gross_income)
    except ValueError:
        print("Please enter valid numbers for rate and hours.")

def calculate_deductions():
    try:
        # Regular Deduction from provided fields
        regular_deduction = (
                float(sss_contribution.get()) +
                float(philhealth_contribution.get()) +
                float(pagibig_contribution.get()) +
                float(income_tax_contribution.get())
        )

        # Other Deduction from provided fields
        other_deduction = (
                float(sss_loan.get()) +
                float(pagibig_loan.get()) +
                float(faculty_savings_deposit.get()) +
                float(faculty_savings_loan.get()) +
                float(salary_loan.get()) +
                float(other_loan.get())
        )

        # Set the calculated values
        regular_deduction_var.set(regular_deduction)
        other_deduction_var.set(other_deduction)

        # Total Deduction calculation
        total_deduction_value = regular_deduction + other_deduction
        total_deduction.set(total_deduction_value)
    except ValueError:
        print("Please enter valid numbers for deductions.")

def calculate_net_income():
    try:
        gross_income = float(gross_income_var.get())
        total_deductions = float(total_deduction.get())
        net_income = gross_income - total_deductions
        net_income_var.set(net_income)
    except ValueError:
        print("Please enter valid numbers for income and deductions.")

def save_employee_data():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Update the employee_details table
        cursor.execute('''UPDATE employee_details SET
                          first_name=?, middle_name=?, last_name=?, civil_status=?, 
                          qualified_dep_status=?, pay_date=?, employee_status=?, designation=?,
                          sss_contribution=?, philhealth_contribution=?, pagibig_contribution=?,
                          income_tax_contribution=?, sss_loan=?, pagibig_loan=?, 
                          faculty_savings_deposit=?, faculty_savings_loan=?, 
                          salary_loan=?, other_loan=?, total_deduction=?, net_income_var=?, gross_income_var=?, basic_rate_hour=?, basic_no_of_hours_cutoff=?, basic_income_compute_both=?,
                          honorarium_rate_hour=?, honorarium_no_of_hours_cutoff=?, honorarium_income_compute_both=?, other_rate_hour=?, other_no_of_hours_cutoff=?, other_income_compute_both=?
                          WHERE employee_number=?''',
                       (first_name.get(), middle_name.get(), last_name.get(), civil_status.get(),
                        qualified_dep_status.get(), pay_date.get(), employee_status.get(), designation.get(),
                        sss_contribution.get(), philhealth_contribution.get(), pagibig_contribution.get(),
                        income_tax_contribution.get(), sss_loan.get(), pagibig_loan.get(),
                        faculty_savings_deposit.get(), faculty_savings_loan.get(),
                        salary_loan.get(), other_loan.get(), total_deduction.get(), net_income_var.get(), gross_income_var.get(),basic_rate_hour.get(), basic_no_of_hours_cutoff.get(), basic_income_compute_both.get(),
                        honorarium_rate_hour.get(), honorarium_no_of_hours_cutoff.get(), honorarium_income_compute_both.get(),  other_rate_hour.get(), other_no_of_hours_cutoff.get(), other_income_compute_both.get(), search_employee_number.get()))

        # Commit changes
        conn.commit()
        conn.close()

        print("Employee data saved successfully.")
    except Exception as e:
        print("Error saving employee data:", e)

def update_employee_data():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''UPDATE employee_details SET
                          first_name=?, middle_name=?, last_name=?, civil_status=?, 
                          qualified_dep_status=?, pay_date=?, employee_status=?, designation=?,
                          sss_contribution=?, philhealth_contribution=?, pagibig_contribution=?,
                          income_tax_contribution=?, sss_loan=?, pagibig_loan=?, 
                          faculty_savings_deposit=?, faculty_savings_loan=?, 
                          salary_loan=?, other_loan=?, gross_income_var=?, net_income_var=?, total_deduction=? , basic_rate_hour=?, basic_no_of_hours_cutoff=?, basic_income_compute_both=?,
                          honorarium_rate_hour=?, honorarium_no_of_hours_cutoff=?, honorarium_income_compute_both=?, other_rate_hour=?, other_no_of_hours_cutoff=?, other_income_compute_both=?
                          WHERE employee_number=?''',
                       (first_name.get(), middle_name.get(), last_name.get(), civil_status.get(),
                        qualified_dep_status.get(), pay_date.get(), employee_status.get(), designation.get(),
                        sss_contribution.get(), philhealth_contribution.get(), pagibig_contribution.get(),
                        income_tax_contribution.get(), sss_loan.get(), pagibig_loan.get(),
                        faculty_savings_deposit.get(), faculty_savings_loan.get(),
                        salary_loan.get(), other_loan.get(), total_deduction.get(), net_income_var.get(), gross_income_var.get(), basic_rate_hour.get(), basic_no_of_hours_cutoff.get(), basic_income_compute_both.get(),
                        honorarium_rate_hour.get(), honorarium_no_of_hours_cutoff.get(), honorarium_income_compute_both.get(),  other_rate_hour.get(), other_no_of_hours_cutoff.get(), other_income_compute_both.get(), search_employee_number.get()))

        conn.commit()
        conn.close()
        print("Employee data updated successfully.")
    except Exception as e:
        print("Error updating employee data:", e)

def search_employee():
    employee_number = search_employee_number.get()
    if not employee_number:
        print("Please enter an employee number.")
        return

    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee_details WHERE employee_number=?', (employee_number,))
        employee = cursor.fetchone()
        conn.close()

        if employee:
            first_name.set(employee[0])
            middle_name.set(employee[1])
            last_name.set(employee[2])
            civil_status.set(employee[7])
            qualified_dep_status.set(employee[10])
            pay_date.set(employee[12])
            employee_status.set(employee[11])
            designation.set(employee[9])
            department.set(employee[8])

            basic_rate_hour.set(employee[25])
            basic_no_of_hours_cutoff.set(employee[26])
            basic_income_compute_both.set(employee[27])
            honorarium_rate_hour.set(employee[28])
            honorarium_no_of_hours_cutoff.set(employee[29])
            honorarium_income_compute_both.set(employee[30])
            other_rate_hour.set(employee[31])
            other_no_of_hours_cutoff.set(employee[32])
            other_income_compute_both.set(employee[33])

            sss_contribution.set(employee[34])
            philhealth_contribution.set(employee[35])
            pagibig_contribution.set(employee[36])
            income_tax_contribution.set(employee[37])
            sss_loan.set(employee[38])
            pagibig_loan.set(employee[39])
            faculty_savings_deposit.set(employee[40])
            faculty_savings_loan.set(employee[41])
            salary_loan.set(employee[42])
            other_loan.set(employee[43])
            total_deduction.set(employee[44])
            gross_income_var.set(employee[45])
            net_income_var.set(employee[46])


        else:
            print("Employee not found.")
    except Exception as e:
        print("Error searching for employee:", e)

# Create the main window
window = tk.Tk()
window.title("Bianca's Choice Payroll")

# Load and resize the image
image = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\Default.jpg')
resized_image = image.resize((150, 150))
employee_image = ImageTk.PhotoImage(resized_image)

# Create frame for basic employee info
frame_choice_payroll = Frame(window, padx=20, pady=20)
frame_choice_payroll.grid(row=1, column=0)

# Bold text for employee basic info
Label(frame_choice_payroll, text="EMPLOYEE BASIC INFO:", font=("Times New Roman", 8, "bold")).grid(row=1, column=0, columnspan=2,
                                                                                         padx=(0, 40), pady=(0, 10))

# Labels and Entry Widgets for basic employee info
first_name = StringVar()
middle_name = StringVar()
last_name = StringVar()
civil_status = StringVar()
qualified_dep_status = StringVar()
pay_date = StringVar()
employee_status = StringVar()
designation = StringVar()
department = StringVar()
sss_contribution = StringVar()
philhealth_contribution = StringVar()
pagibig_contribution = StringVar()
income_tax_contribution = StringVar()
sss_loan = StringVar()
pagibig_loan = StringVar()
faculty_savings_deposit = StringVar()
faculty_savings_loan = StringVar()
salary_loan = StringVar()
other_loan = StringVar()
total_deduction = StringVar()
basic_rate_hour = StringVar()
basic_no_of_hours_cutoff = StringVar()
honorarium_rate_hour = StringVar()
honorarium_no_of_hours_cutoff = StringVar()
other_rate_hour = StringVar()
basic_income_compute = StringVar()
basic_income_compute_both = StringVar()
honorarium_income_compute = StringVar ()
honorarium_income_compute_both = StringVar()
other_income_compute = StringVar()
other_income_compute_both = StringVar()
other_no_of_hours_cutoff = StringVar()
income_cutoff = StringVar()
gross_income_var= StringVar()
gross_income_compute = StringVar()
net_income_var = StringVar()
basic_income_var = StringVar()
honorarium_income_var = StringVar()
other_income_var = StringVar()
regular_deduction_var = StringVar()
other_deduction_var = StringVar()

# Labels and Entry Widgets for basic employee info
Label(frame_choice_payroll, text="Firstname:").grid(row=1, column=2, sticky=E, padx=(150,10),pady=(30, 5))
Label(frame_choice_payroll, text="Middle Name:").grid(row=2, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Surname:").grid(row=3, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Civil Status:").grid(row=4, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Qualified Dependents Status:").grid(row=5, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Paydate:").grid(row=6, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Employee Status:").grid(row=7, column=2, sticky=E, pady=5)
Label(frame_choice_payroll, text="Designation:").grid(row=8, column=2, sticky=E, pady=(5, 20))

# Entry widgets
Entry(frame_choice_payroll, textvariable=first_name).grid(row=1, column=3, pady=(30, 5))
Entry(frame_choice_payroll, textvariable=middle_name).grid(row=2, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=last_name).grid(row=3, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=civil_status).grid(row=4, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=qualified_dep_status).grid(row=5, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=pay_date).grid(row=6, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=employee_status).grid(row=7, column=3, pady=5)
Entry(frame_choice_payroll, textvariable=designation).grid(row=8, column=3, pady=(5, 20))

Label(frame_choice_payroll, text="REGULAR DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=9, column=2, sticky=E, pady=5)

# Placeholder entries for Contributions, Loans, and Deductions
Label(frame_choice_payroll, text="SSS Contribution:").grid(row=10, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=sss_contribution).grid(row=10, column=3, pady=5)
Label(frame_choice_payroll, text="Philhealth Contribution:").grid(row=11, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=philhealth_contribution).grid(row=11, column=3, pady=5)
Label(frame_choice_payroll, text="Pagibig Contribution:").grid(row=12, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=pagibig_contribution).grid(row=12, column=3, pady=5)
Label(frame_choice_payroll, text="Income Tax Contribution:").grid(row=13, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=income_tax_contribution).grid(row=13, column=3, pady=5)

Label(frame_choice_payroll, text="OTHER DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=14, column=2, sticky=E, pady=5)

Label(frame_choice_payroll, text="SSS Loan:").grid(row=15, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=sss_loan).grid(row=15, column=3, pady=5)
Label(frame_choice_payroll, text="Pag-ibig Loan:").grid(row=16, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=pagibig_loan).grid(row=16, column=3, pady=5)
Label(frame_choice_payroll, text="Faculty Savings Deposit:").grid(row=17, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=faculty_savings_deposit).grid(row=17, column=3, pady=5)
Label(frame_choice_payroll, text="Faculty Savings Loan:").grid(row=18, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=faculty_savings_loan).grid(row=18, column=3, pady=5)
Label(frame_choice_payroll, text="Salary Loan:").grid(row=19, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=salary_loan).grid(row=19, column=3, pady=5)
Label(frame_choice_payroll, text="Other Loan:").grid(row=20, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=other_loan).grid(row=20, column=3, pady=5)


Label(frame_choice_payroll, text="DEDUCTION SUMMARY:", font=("Arial", 10, "bold")).grid(row=21, column=2, sticky=E, pady=5)


Label(frame_choice_payroll, text="Total Deduction:").grid(row=22, column=2, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=total_deduction).grid(row=22, column=3, pady=5)

# Additional Buttons
Button(frame_choice_payroll, text="GROSS INCOME", command=calculate_gross_income, bg="dark blue").grid(row=23, column=2, padx=(30, 5), pady=5, sticky=W)
Button(frame_choice_payroll, text="NET INCOME", command=calculate_net_income, bg="blue").grid(row=23, column=2, padx=(130, 0), pady=5, sticky=W)
Button(frame_choice_payroll, text="SAVE", command=save_employee_data, bg="orange").grid(row=23, column=3, padx=(0, 0), pady=5, sticky=W)
Button(frame_choice_payroll, text="UPDATE", command=update_employee_data, bg="purple").grid(row=23, column=3, padx=(40, 0), pady=5, sticky=W)
Button(frame_choice_payroll, text="DEDUCTIONS", command=calculate_deductions, bg="yellow").grid(row=23, column=3, padx=(100, 0), pady=5, sticky=W)


# Add employee image with padding
Label(frame_choice_payroll, image=employee_image).grid(row=1, column=0, rowspan=6, columnspan=2, padx=(0, 10), pady=(30, 0), sticky=N)

# Search functionality
search_employee_number = StringVar()

Label(frame_choice_payroll, text="Department:").grid(row=8, column=0, sticky=E, pady=(20, 5))
Entry(frame_choice_payroll).grid(row=8, column=1, padx=(0,50), pady=(20, 5))


# Basic Income Section
Label(frame_choice_payroll, text="BASIC INCOME:", font=("Arial", 10, "bold")).grid(row=9, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Rate/ Hour:").grid(row=10, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="No of Hours/ Cut off:").grid(row=11, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Income/ Cut off:").grid(row=12, column=0, sticky=E, pady=5)


Entry(frame_choice_payroll, textvariable=basic_rate_hour).grid(row=10, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=basic_no_of_hours_cutoff).grid(row=11, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=basic_income_compute_both).grid(row=12, column=1, padx=(0,50), pady=5)

# Honorarium Section
Label(frame_choice_payroll, text="HONORARIUM INCOME:", font=("Arial", 10, "bold")).grid(row=13, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Rate/ Hour:").grid(row=14, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="No of Hours/ Cut off:").grid(row=15, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Income/ Cut off:").grid(row=16, column=0, sticky=E, pady=5)

Entry(frame_choice_payroll, textvariable=honorarium_rate_hour).grid(row=14, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=honorarium_no_of_hours_cutoff).grid(row=15, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=honorarium_income_compute_both).grid(row=16, column=1, padx=(0,50), pady=5)

# Other Income Section
Label(frame_choice_payroll, text="OTHER INCOME:", font=("Arial", 10, "bold")).grid(row=17, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Rate/ Hour:").grid(row=18, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="No of Hours/ Cut off:").grid(row=19, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Income/ Cut off:").grid(row=20, column=0, sticky=E, pady=5)

Entry(frame_choice_payroll, textvariable=other_rate_hour).grid(row=18, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=other_no_of_hours_cutoff).grid(row=19, column=1, padx=(0,50), pady=5)
Entry(frame_choice_payroll, textvariable=other_income_compute_both).grid(row=20, column=1, padx=(0,50), pady=5)

# Summary Section
Label(frame_choice_payroll, text="SUMMARY INCOME:", font=("Arial", 10, "bold")).grid(row=21, column=0, sticky=E, pady=5)
Label(frame_choice_payroll, text="Gross Income:").grid(row=22, column=0, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=gross_income_var).grid(row=22, column=1, pady=5)
Label(frame_choice_payroll, text="Net Income:").grid(row=23, column=0, sticky=E, pady=5)
Entry(frame_choice_payroll, textvariable=net_income_var).grid(row=23, column=1, pady=5)

search_frame = Frame(window, padx=20, pady=0)
search_frame.grid(row=1, column=0, padx=(0, 50), pady=(20, 330), sticky=W)
Label(search_frame, text="Employee Number:").grid(row=6, column=0, sticky=E, pady=(20, 5))
Entry(search_frame, textvariable=search_employee_number).grid(row=6, column=1, padx=(0, 50), pady=(20, 5))
Button(search_frame, text="Search", command=search_employee, bg="Blue").grid(row=7, column=1, padx=(0, 50), pady=5, sticky=W)

# Labels and Entry Widgets for payroll info
Label(window, text="Bianca's Choice Payroll", font=("Arial", 30, "bold")).grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

# Run the application
window.mainloop()


