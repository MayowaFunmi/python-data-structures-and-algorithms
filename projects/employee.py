import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import psycopg2
import employee_backend


class Employee:
    def __init__(self, root):
        self.root = root
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        # print(width)
        self.root.geometry("%dx%d" % (width, height))
        #self.root.attributes('-fullscreen', True)
        self.root.title('Employee Management System')
        self.root.rowconfigure(0, weight=1, minsize=50)
        #self.root.columnconfigure(2, weight=1, minsize=75)
        self.var_id = StringVar()
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()
        self.var_com_search = StringVar()
        self.var_search = StringVar()

        lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('Poppins', 37, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1350, height=50)

        # logo
        img_logo = Image.open('projects/images/contact.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=150, y=0, width=50, height=50)

        # image frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1350, height=160)

        # 1st
        img1 = Image.open('projects/images/employees1.jpeg')
        img1 = img1.resize((450, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=450, height=160)

        # 2nd
        img2 = Image.open('projects/images/employees2.png')
        img2 = img2.resize((450, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=450, y=0, width=450, height=160)

        # 3rd
        img3 = Image.open('projects/images/employees3.jpeg')
        img3 = img3.resize((450, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=900, y=0, width=450, height=160)

        # main frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=0, y=210, width=1350, height=560)

        # upper frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information', font=('Poppins', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=0, width=1350, height=230)

        # labels and entry fields
        global combo_dep
        global txt_name
        global txt_description
        global txt_email
        global txt_address
        global com_txt_married
        global txt_dob
        global txt_doj
        global com_txt_proof
        global txt_proof
        global com_txt_gender
        global txt_phone
        global txt_country
        global txt_salary
        global btn_add

        lbl_dep = Label(upper_frame, text='Department:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('Poppins', 12, 'bold'), width=15, state='readonly')
        combo_dep['value'] = ('Department', 'HR', 'Software Engineer', 'Manager')    # write function to generate values
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # name
        lbl_name = Label(upper_frame, text='Name:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=15, font=('Poppins', 11, 'bold'))
        txt_name.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # designation
        lbl_designation = Label(upper_frame, text='Designation:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_designation.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_description = ttk.Entry(upper_frame, textvariable=self.var_designation, width=15, font=('Poppins', 11, 'bold'))
        txt_description.grid(row=1, column=1, padx=2, pady=7)

        # email
        lbl_email = Label(upper_frame, text='Email:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_email.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=15, font=('Poppins', 11, 'bold'))
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        # address
        lbl_address = Label(upper_frame, text='Address:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_address.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=15, font=('Poppins', 11, 'bold'))
        txt_address.grid(row=2, column=1, padx=2, pady=7)

        # married
        lbl_married_status = Label(upper_frame, text='Marital Status:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_married_status.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        com_txt_married = ttk.Combobox(upper_frame, textvariable=self.var_married, state='readonly', font=('Poppins', 12, 'bold'), width=15)
        com_txt_married['value']=('Married', 'Single', 'Divorced', 'In A Relationship', 'Complicated')
        com_txt_married.current(0)
        com_txt_married.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # dob
        lbl_dob = Label(upper_frame, text='Date Of Birth:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_dob.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        txt_dob = DateEntry(upper_frame, textvariable=self.var_dob, width=15, background="magenta3", foreground="white", bd=2)
        txt_dob.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # doj
        lbl_doj = Label(upper_frame, text='Date Joined:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_doj.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        txt_doj = DateEntry(upper_frame, textvariable=self.var_doj, width=15, background="magenta3", foreground="white", bd=2)
        txt_doj.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # id proof
        com_txt_proof = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb, state='readonly', font=('Poppins', 12, 'bold'), width=15)
        com_txt_proof['value'] = ('Identification', 'National ID Card', 'International Passport', 'Drivers Licence', 'Voters Card')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_proof = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=15, font=('Poppins', 11, 'bold'))
        txt_proof.grid(row=4, column=1, padx=2, pady=7) # add a placeholder here to add id number

        # gender
        lbl_gender = Label(upper_frame, text='Gender:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_gender.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        com_txt_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, state='readonly', font=('Poppins', 12, 'bold'), width=15)
        com_txt_gender['value'] = ('Male', 'Female')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # phone
        lbl_phone = Label(upper_frame, text='Phone No.:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_phone.grid(row=0, column=5, padx=2, pady=7, sticky=W)

        txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=15, font=('Poppins', 11, 'bold'))
        txt_phone.grid(row=0, column=6, padx=2, pady=7)

        # country
        lbl_country = Label(upper_frame, text='Country:', font=('Poppins', 12, 'bold'), bg='white')
        lbl_country.grid(row=1, column=5, padx=2, pady=7, sticky=W)

        txt_country = ttk.Entry(upper_frame, textvariable=self.var_country, width=15, font=('Poppins', 11, 'bold'))
        txt_country.grid(row=1, column=6, padx=2, pady=7)

        # salary
        lbl_salary = Label(upper_frame, text='Salary(N):', font=('Poppins', 12, 'bold'), bg='white')
        lbl_salary.grid(row=2, column=5, padx=2, pady=7, sticky=W)

        txt_salary = ttk.Entry(upper_frame, textvariable=self.var_salary, width=15, font=('Poppins', 11, 'bold'))
        txt_salary.grid(row=2, column=6, padx=2, pady=7)

        # masked image
        img_mask = Image.open('projects/images/employees2.png')
        img_mask = img_mask.resize((170, 170), Image.ANTIALIAS)
        self.photo_mask = ImageTk.PhotoImage(img_mask)

        self.img_mask = Label(upper_frame, image=self.photo_mask)
        self.img_mask.place(x=1000, y=0, width=170, height=170)

        # button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1200, y=5, width=100, height=180)

        btn_add = Button(button_frame, text='Save', command=self.add_employee, font=('Poppins', 10, 'bold'), width=10, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=0, pady=5)

        btn_update = Button(button_frame, text='Update', font=('Poppins', 10, 'bold'), width=10, bg='blue', fg='white', command=self.update_data)
        btn_update.grid(row=1, column=0, padx=0, pady=5)

        btn_delete = Button(button_frame, text='Delete', font=('Poppins', 10, 'bold'), width=10, bg='blue', fg='white', command=self.delete)
        btn_delete.grid(row=2, column=0, padx=0, pady=5)

        btn_clear = Button(button_frame, text='Clear', font=('Poppins', 10, 'bold'), width=10, bg='blue', fg='white', command=self.clear_fields)
        btn_clear.grid(row=3, column=0, padx=0, pady=5)

        # down frame
        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table',
                                font=('Poppins', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=230, width=1350, height=250)

        # search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information',
                                  font=('Poppins', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1340, height=60)

        search_by = Label(search_frame, font=('arial', 11, 'bold'), text='Search By:', fg='white', bg='red')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, state='readonly', font=('arial', 12, 'bold'), width=18)
        com_txt_search['value'] = ('Select Option', 'Department', 'Name', 'Designation', 'Email', 'Marital Status', 'Date Of Birth', 'Date Joined', 'ID Type', 'ID Value', 'Gender', 'Phone', 'Country', 'Salary')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('arial', 11, 'bold'))
        txt_search.grid(row=0, column=2, padx=5)

        btn__search = Button(search_frame, text='Search', command=self.search_data, font=('arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn__search.grid(row=0, column=3, padx=5)

        btn_showAll = Button(search_frame, command=self.fetch_data, text='Show All', font=('arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn_showAll.grid(row=0, column=4, padx=5)

        stayhome = Label(search_frame, text='Wear A Mask', font=('times new roman', 30, 'bold'), fg='red', bg='white')
        stayhome.place(x=780, y=0, width=600, height=30)

        img_logo_mask = Image.open('projects/images/employees2.png')
        img_logo_mask = img_logo_mask.resize((50, 50), Image.ANTIALIAS)
        self.photoimg_logo_mask = ImageTk.PhotoImage(img_logo_mask)

        self.logo = Label(search_frame, image=self.photoimg_logo_mask)
        self.logo.place(x=900, y=0, width=50, height=30)

        #===================== Employee Table ===========================
        # Table Frame

        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1310, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=('S/N', 'Dept', 'Name', 'Desg', 'Email', 'Address', 'Married', 'DoB', 'Joined', 'ID', 'ID Number', 'Gender', "Phone", 'Country', 'Salary'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('S/N', text='S/N')
        self.employee_table.heading('Dept', text='Department')
        self.employee_table.heading('Name', text='Name')
        self.employee_table.heading('Desg', text='Designation')
        self.employee_table.heading('Email', text='Email')
        self.employee_table.heading('Address', text='Address')
        self.employee_table.heading('Married', text='Marital Status')
        self.employee_table.heading('DoB', text='Date Of Birth')
        self.employee_table.heading('Joined', text='Date Joined')
        self.employee_table.heading('ID', text='Identity')
        self.employee_table.heading('ID Number', text='ID Number')
        self.employee_table.heading('Gender', text='Gender')
        self.employee_table.heading('Phone', text='Phone')
        self.employee_table.heading('Country', text='Country')
        self.employee_table.heading('Salary', text='Salary')

        self.employee_table['show'] = 'headings'
        self.employee_table.column('S/N', width=75)
        self.employee_table.column('Dept', width=150)
        self.employee_table.column('Name', width=150)
        self.employee_table.column('Desg', width=150)
        self.employee_table.column('Email', width=200)
        self.employee_table.column('Address', width=150)
        self.employee_table.column('Married', width=200)
        self.employee_table.column('DoB', width=200)
        self.employee_table.column('Joined', width=150)
        self.employee_table.column('ID', width=150)
        self.employee_table.column('ID Number', width=150)
        self.employee_table.column('Gender', width=150)
        self.employee_table.column('Phone', width=150)
        self.employee_table.column('Country', width=150)
        self.employee_table.column('Salary', width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()
    # =============== Function Declaration ========================

    def clear_fields(self):
        combo_dep.current(0)    # self.var_dep.set('Department')
        txt_name.delete(0, END) # self.var_name.set('')
        txt_description.delete(0, END)
        txt_email.delete(0, END)
        txt_address.delete(0, END)
        com_txt_married.current(0)
        com_txt_proof.current(0)
        txt_proof.delete(0, END)
        com_txt_gender.current(0)
        txt_phone.delete(0, END)
        txt_country.delete(0, END)
        txt_salary.delete(0, END)
        btn_add['state'] = 'normal'

    def add_employee(self):
        if self.var_dep.get() == '' or self.var_name.get() == '' or self.var_designation.get() == '' or self.var_email.get() == '' or \
                self.var_address.get() == '' or self.var_married.get() == '' or self.var_dob.get() == '' or self.var_doj.get() == '' or \
                self.var_idproof.get() == '' or self.var_idproofcomb.get() == '' or self.var_gender.get() == '' or self.var_phone.get() == '' or \
                self.var_country.get() == '' or self.var_salary.get() == '':
            messagebox.showerror('Error', 'All fields are required!')
        else:
            employee_backend.employee_data(
                self.var_dep.get(),
                self.var_name.get(),
                self.var_designation.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_married.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_idproofcomb.get(),
                self.var_idproof.get(),
                self.var_gender.get(),
                self.var_phone.get(),
                self.var_country.get(),
                self.var_salary.get(),
            )
            self.fetch_data()
            # clear all fields
            self.clear_fields()
            messagebox.showinfo('Added Successfully', 'Employee Data Has Been Added')

    # fetch data
    def fetch_data(self):
        conn = sqlite3.connect('projects/employee.db')
        cursor = conn.cursor()
        cursor.execute('SELECT oid, * FROM employee_table')
        data = cursor.fetchall()

        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert('', END, values=i)
        conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self, event=''):
        btn_add['state'] = 'disabled'
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        global id
        id = data[0]
        self.var_dep.set(data[1])
        self.var_name.set(data[2]),
        self.var_designation.set(data[3]),
        self.var_email.set(data[4]),
        self.var_address.set(data[5]),
        self.var_married.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_doj.set(data[8]),
        self.var_idproofcomb.set(data[9]),
        self.var_idproof.set(data[10]),
        self.var_gender.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_country.set(data[13]),
        self.var_salary.set(data[14]),

    # update data
    def update_data(self):
        if self.var_dep.get() == '' or self.var_name.get() == '' or self.var_designation.get() == '' or self.var_email.get() == '' or \
                self.var_address.get() == '' or self.var_married.get() == '' or self.var_dob.get() == '' or self.var_doj.get() == '' or \
                self.var_idproof.get() == '' or self.var_idproofcomb.get() == '' or self.var_gender.get() == '' or self.var_phone.get() == '' or \
                self.var_country.get() == '' or self.var_salary.get() == '':
            messagebox.showerror('Error', 'All fields are required!')
        else:
            update = messagebox.askyesno('Update Data', 'Update This Employee Data?')
            if update > 0:
                conn = sqlite3.connect('projects/employee.db')
                cursor = conn.cursor()
                cursor.execute("""UPDATE employee_table SET
                    department = :department,
                    name = :name,
                    designation = :designation,
                    email = :email,
                    address = :address,
                    marital_status = :marital_status,
                    date_of_birth = :date_of_birth,
                    date_joined = :date_joined,
                    id_type = :id_type,
                    id_value = :id_value,
                    gender = :gender,
                    phone = :phone,
                    country = :country,
                    salary = :salary
                    WHERE oid = :oid""",

                    {
                        'department': self.var_dep.get(),
                        'name': self.var_name.get(),
                        'designation': self.var_designation.get(),
                        'email': self.var_email.get(),
                        'address': self.var_address.get(),
                        'marital_status': self.var_married.get(),
                        'date_of_birth': self.var_dob.get(),
                        'date_joined': self.var_doj.get(),
                        'id_type': self.var_idproofcomb.get(),
                        'id_value': self.var_idproof.get(),
                        'gender': self.var_gender.get(),
                        'phone': self.var_phone.get(),
                        'country': self.var_country.get(),
                        'salary': self.var_salary.get(),
                        'oid': id
                    })
                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo('Update Successful', 'Employee Data Has Been Updated!!!', parent=self.root)
                btn_add['state'] = 'normal'

            else:
                if not update:
                    return

    # delete
    def delete(self):
        if self.var_dep.get() == '' or self.var_name.get() == '' or self.var_designation.get() == '' or self.var_email.get() == '' or \
                self.var_address.get() == '' or self.var_married.get() == '' or self.var_dob.get() == '' or self.var_doj.get() == '' or \
                self.var_idproof.get() == '' or self.var_idproofcomb.get() == '' or self.var_gender.get() == '' or self.var_phone.get() == '' or \
                self.var_country.get() == '' or self.var_salary.get() == '':
            messagebox.showerror('Error', 'Select An Employee Data To Delete. All Fields Required')
        else:
            delete = messagebox.askyesno('Delete Data', 'Delete This Employee Data?', parent=self.root)
            if delete > 0:
                conn = sqlite3.connect('projects/employee.db')
                cursor = conn.cursor()

                cursor.execute("DELETE FROM employee_table WHERE oid= " + str(id))

                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo('Delete Successful', 'Employee Data Has Been Deleted!!!', parent=self.root)

    # search

    def search_data(self):
        if self.var_com_search.get() == 'Select Option' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please Select An Option')
        else:
            try:
                search_option = self.var_com_search.get()
                search = employee_backend.rename(search_option)
                print(search)
                search_val = self.var_search.get()
                print(search_val)

                conn = sqlite3.connect('projects/employee.db')
                cursor = conn.cursor()

                cursor.execute("SELECT oid, * FROM employee_table WHERE " + search + " = " + search_val)

                rows = cursor.fetchall()
                print(rows)
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert('', END, values=i)
                else:
                    messagebox.showerror('Error', 'Data Not Found!!!', parent=self.root)

                conn.commit()
                conn.close()
            except:
                messagebox.showerror('Error', 'Something went wrong')


if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()