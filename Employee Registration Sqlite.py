import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
from tkinter import filedialog

# Function to save employee data to SQLite database
def save_employee():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_details (
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            suffix TEXT,
            date_of_birth TEXT,
            gender TEXT,
            nationality TEXT,
            civil_status TEXT,
            department TEXT,
            designation TEXT,
            qualified_dep_status TEXT,
            employee_status TEXT,
            pay_date TEXT,
            employee_number TEXT PRIMARY KEY,
            contact_no TEXT,
            email TEXT,
            social_media TEXT,
            social_media_account_id TEXT,
            address_line1 TEXT,
            address_line2 TEXT,
            city_municipality TEXT,
            state_province TEXT,
            country TEXT,
            zip_code TEXT,
            picture_path TEXT
        )
        ''')

        # Insert data into the table
        cursor.execute('''
            INSERT INTO employee_details (
                first_name, middle_name, last_name, suffix, date_of_birth, gender,
                nationality, civil_status, department, designation, qualified_dep_status,
                employee_status, pay_date, employee_number, contact_no, email,
                social_media, social_media_account_id, address_line1, address_line2,
                city_municipality, state_province, country, zip_code, picture_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
            FirstName1.get(), MiddleName.get(), LastName.get(), Suffix.get(),
            DateOfBirth.get(), gender_var.get(), nationality_var.get(), civil_status_var.get(),
            Department.get(), Designation.get(), qualified_dep_var.get(), EmployeeStatus.get(),
            PayDate.get(), EmployeeNumber.get(), Contact.get(), Email.get(), social_media_var.get(),
            SocialMediaAccID.get(), Address1.get(), Address2.get(), CityMunicipality.get(),
            StateProvince.get(), country_var.get(), ZipCode.get(), PicturePath.get()
        ))



        conn.commit()
        conn.close()

        print("Employee data has been successfully saved.")

    except Exception as e:
        print("Error saving employee data:", e)

# Function to handle file selection
def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        PicturePath.delete(0, END)
        PicturePath.insert(0, file_path)

# Create the GUI
window = tk.Tk()
window.title("HAKU'S EMPLOYEE PERSONAL INFORMATION")
window.configure(bg='dark olive green')

# Create the heading label with modified properties
heading = Label(text="HAKU'S EMPLOYEE PERSONAL INFORMATION", fg='white', bg='dark olive green', font=('Times New Roman', 20, 'bold'))
heading.place(x=15, y=30, width=990)

# Load and resize the image
image1 = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\haku.png')
resized_image = image1.resize((90, 90))
employee_image = ImageTk.PhotoImage(resized_image)

# Create frame for user account info
user_frame = Frame(window, padx=20, pady=20)
user_frame.grid(row=1, column=0, sticky="ew")

frame = Frame(window, width=675, height=110, bg='light gray').place(x=150, y=150)
Button(frame, width=10, pady=4, text='Choose file', bg='white', fg='black', cursor='hand2', border=1).place(x=160, y=200)
NF = Label(frame, text='No File Chosen', bg='light gray', font=('black',7))
NF.place(x=160,y=235)

ContactInfo1 = Label(text='Contact Info', fg='white', bg='dark olive green', font=('black',9, 'bold'))
ContactInfo1.place(x=148,y=404)

## Add user image with padding
image_label = Label(window, image=employee_image)
image_label.place(x=165, y=100)

FN = Label(frame, text='First Name', bg='light gray', font=('black',9))
FN.place(x=290,y=158)
FirstName1=Entry(frame, width=22, border=1, fg='black', bg='white')
FirstName1.place(x=290,y=180)

MiddleName1 = Label(frame, text='Middle Name', bg='light gray', font=('black',9))
MiddleName1.place(x=430,y=158)
MiddleName=Entry(frame, width=22, border=1, fg='black', bg='white')
MiddleName.place(x=430,y=180)

LastName1 = Label(frame, text='Last Name', bg='light gray', font=('black',9))
LastName1.place(x=570,y=158)
LastName=Entry(frame, width=19, border=1, fg='black', bg='white')
LastName.place(x=570,y=180)

Suffix1 = Label(frame, text='Suffix', bg='light gray', font=('black',9))
Suffix1.place(x=695,y=158)
Suffix=Entry(frame, width=17, border=1, fg='black', bg='white')
Suffix.place(x=695,y=180)

DateOfBirth1 = Label(frame, text='Date of Birth', bg='light gray', font=('black',9))
DateOfBirth1.place(x=290, y=200)

DateOfBirth = DateEntry(frame, width=19, border=1, fg='black', bg='white', date_pattern="yyyy-mm-dd")
DateOfBirth.place(x=290, y=223)


Gender1 = Label(frame, text='Gender', bg='light gray', font=('black',9))
Gender1.place(x=435,y=200)
gender_var = StringVar(window)
gender_var.set("Select One")
gender_choices = ['Select One','Male', 'Female', 'Other']
Gender = OptionMenu(frame, gender_var, *gender_choices)
Gender.config(width=11, height=1, border=1, bg='white')
Gender.place(x=435, y=223)

Nationality1 = Label(frame, text='Nationality', bg='light gray', font=('black',9))
Nationality1.place(x=550,y=200)
nationality_var = StringVar(window)
nationality_var.set("Select One")
nationality_choices = ['Select One','Filipino', 'American', 'Japanese', 'Korean', 'Other']
Nationality = OptionMenu(frame, nationality_var, *nationality_choices)
Nationality.config(width=8, height=1, border=1, bg='white')
Nationality.place(x=550, y=223)

CivilStatus1 = Label(frame, text='Civil Status', bg='light gray', font=('black',9))
CivilStatus1.place(x=650,y=200)
civil_status_var = StringVar(window)
civil_status_var.set("Select One")
civil_status_choices = ['Select One','Single', 'Married', 'Widowed', 'Divorced', 'Other']
CivilStatus = OptionMenu(frame, civil_status_var, *civil_status_choices)
CivilStatus.config(width=18, height=1, border=1, bg='white')
CivilStatus.place(x=650, y=223)


frame2 = Frame(window, width=675, height=130, bg='light gray').place(x=150, y=275)
Department1 = Label(frame, text='Department', bg='light gray', font=('black',9))
Department1.place(x=165,y=283)
Department=Entry(frame, width=45, border=1, fg='black', bg='white')
Department.place(x=165,y=305)

Designation1 = Label(frame, text='Designation', bg='light gray', font=('black',9))
Designation1.place(x=440,y=283)
Designation=Entry(frame, width=27, border=1, fg='black', bg='white')
Designation.place(x=445,y=305)

QualitfiedDepStatus1 = Label(frame, text='Qualified Dep. Status', bg='light gray', font=('black',9))
QualitfiedDepStatus1.place(x=615,y=283)
qualified_dep_var = StringVar(window)
qualified_dep_var.set("Select One")
qualified_dep_choices = ['Select One','Approved', 'Declined', 'Pending Review']
QualifiedDepStatus = OptionMenu(frame, qualified_dep_var, *qualified_dep_choices)
QualifiedDepStatus.config(width=23, height=1, bg='white', border=1)
QualifiedDepStatus.place(x=615, y=305)

EmployeeStatus1 = Label(frame, text='Employee Status', bg='light gray', font=('black',9))
EmployeeStatus1.place(x=165,y=338)
EmployeeStatus=Entry(frame, width=47, border=1, fg='black', bg='white')
EmployeeStatus.place(x=165,y=365)

PayDate1 = Label(frame, text='PayDate', bg='light gray', font=('black',9))
PayDate1.place(x=455, y=338)

PayDate = DateEntry(frame, width=16, border=1, fg='black', bg='white', date_pattern="yyyy-mm-dd")
PayDate.place(x=455, y=365)


EmployeeNumber1 = Label(frame, text='Employee Number', bg='light gray', font=('black',9))
EmployeeNumber1.place(x=580,y=338)
EmployeeNumber=Entry(frame, width=36, border=1, fg='black', bg='white')
EmployeeNumber.place(x=580,y=365)


frame3 = Frame(window, width=675, height=125, bg='light gray').place(x=150, y=425)
Contact1 = Label(frame, text='Contact No.', bg='light gray', font=('black',9))
Contact1.place(x=165,y=435)
Contact=Entry(frame, width=45, border=1, fg='black', bg='white')
Contact.place(x=165,y=460)

Email1 = Label(frame, text='Email', bg='light gray', font=('black',9))
Email1.place(x=445,y=435)
Email=Entry(frame, width=58, border=1, fg='black', bg='white')
Email.place(x=445,y=460)

Other1 = Label(frame, text='Other (Social Media)', bg='light gray', font=('black',9))
Other1.place(x=165,y=485)
social_media_var = StringVar(window)
social_media_var.set("Select One")
social_media_choices = ['Select One','Instagram', 'Facebook', 'Twitter', 'Other']
Other = OptionMenu(frame, social_media_var, *social_media_choices)
Other.config(width=38, height=1, border=1, bg='white')
Other.place(x=165, y=510)

SocialMediaAccID1 = Label(frame, text='Social Media Account ID/No.', bg='light gray', font=('black',9))
SocialMediaAccID1.place(x=445,y=485)
SocialMediaAccID=Entry(frame, width=58, border=1, fg='black', bg='white')
SocialMediaAccID.place(x=445,y=510)


frame4 = Frame(window, width=675, height=310, bg='light gray').place(x=150, y=575)
AddressInfo1 = Label(frame, text='Address', fg='white', bg='dark olive green', font=('black',9, "bold"))
AddressInfo1.place(x=148,y=553)
Address11 = Label(frame, text='Address Line 1', bg='light gray', font=('black',9))
Address11.place(x=165,y=590)
Address1=Entry(frame, width=105, border=1, fg='black', bg='white')
Address1.place(x=165,y=615)

Address21 = Label(frame, text='Address Line 2', bg='light gray', font=('black',9))
Address21.place(x=165,y=640)
Address2=Entry(frame, width=85, border=1, fg='black', bg='white')
Address2.place(x=165,y=665)

CityMunicipality1 = Label(frame, text='City/Municipality', bg='light gray', font=('black',9))
CityMunicipality1.place(x=165,y=690)
CityMunicipality=Entry(frame, width=50, border=1, fg='black', bg='white')
CityMunicipality.place(x=165,y=720)

StateProvince1 = Label(frame, text='State/Province', bg='light gray', font=('black',9))
StateProvince1.place(x=475,y=690)
StateProvince=Entry(frame, width=53, border=1, fg='black', bg='white')
StateProvince.place(x=475,y=720)

Country1 = Label(frame, text='Country', bg='light gray', font=('black',9))
Country1.place(x=165,y=745)
country_var = StringVar(window)
country_var.set("Select One")
country_choices = ['Select One','Philippines', 'US', 'Japan', 'Korea', 'Other']
Country = OptionMenu(frame, country_var, *country_choices)
Country.config(width=43, height=1, border=1, bg='white')
Country.place(x=165, y=770)

ZipCode1 = Label(frame, text='Zip Code', bg='light gray', font=('black',9))
ZipCode1.place(x=475,y=745)
ZipCode=Entry(frame, width=33, border=1, fg='black', bg='white')
ZipCode.place(x=475,y=770)

PicturePath1 = Label(frame, text='Picture Path', bg='light gray', font=('black',9))
PicturePath1.place(x=165,y=800)
PicturePath=Entry(frame, width=105, border=1, fg='black', bg='white')
PicturePath.place(x=165,y=825)


# Function to handle canceling the operation
def cancel_operation():
    window.destroy()

# Save and Cancel buttons
SaveButton = Button(window, text="Save", bg='dark green', fg='black', width=13, font=('Times New Roman', 8), command=save_employee)
SaveButton.place(x=150, y=900)

CancelButton = Button(window, text="Cancel", bg='light green', fg='black', width=13, border=1, font=('Times New Roman', 8), command=cancel_operation)
CancelButton.place(x=250, y=900)

window.geometry('950x1000')
window.mainloop()

