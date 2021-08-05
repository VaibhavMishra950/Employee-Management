#Importing Dependencies.
from tkinter import *
import tkinter.scrolledtext as st
from tkinter import messagebox as mb
import mysql.connector as sql



def update_employee():
	if (ent_name_update.get() == "" or ent_post_update.get() == "" or gender_var_update.get() == "" or ent_salary_update.get() == "" or ent_mobile_update.get() == ""):
		mb.showerror("Employee Management", "All Fields Require At Least One Value.")
	else:
		cursor.execute("update employee set name = '{}', post = '{}', gender = '{}', salary = {}, mobile = {} where empid = {}".format(ent_name_update.get(), ent_post_update.get(), gender_var_update.get(),ent_salary_update.get(), ent_mobile_update.get(), ent_empid_update['text']))
		con.commit()
		mb.showinfo("Employee Management", "Employee Details Updated Successfully!")
		win_update_employee.destroy(); temp_ent_empid_win.destroy()

def update_employee_win():
	global ent_gender_update_male
	global ent_gender_update_female
	global ent_empid_update
	global ent_name_update
	global ent_post_update
	global ent_salary_update
	global ent_mobile_update
	global gender_var_update
	global win_update_employee
	win_update_employee = Tk()
	win_update_employee.title("Update Employee Details")
	
	
	frm_ent_data_update = LabelFrame(win_update_employee, text = "Update Details")
	frm_ent_data_update.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	frm_buttons = Frame(win_update_employee)
	frm_buttons.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	lbl_empid_update = Label(frm_ent_data_update, text = "Employee\'s ID: ", font = ("Product Sans", 10))
	lbl_empid_update.grid(row = 0, column = 0, padx = 10, pady = 10)
	ent_empid_update = Label(frm_ent_data_update, text = "", font = ("Product Sans", 10))
	ent_empid_update.grid(row = 0, column = 1, padx = 10, pady = 10)
	
	lbl_name_update = Label(frm_ent_data_update, text = "Employee\'s Name: ", font = ("Product Sans", 10))
	lbl_name_update.grid(row = 1, column = 0, padx = 10, pady = 10)
	ent_name_update = Entry(frm_ent_data_update, font = ("Product Sans", 10))
	ent_name_update.grid(row = 1, column = 1, padx = 10, pady = 10)
	
	lbl_post_update = Label(frm_ent_data_update, text = "Employee\'s Post: ", font = ("Product Sans", 10))
	lbl_post_update.grid(row = 2, column = 0, padx = 10, pady = 10)
	ent_post_update = Entry(frm_ent_data_update, font = ("Product Sans", 10))
	ent_post_update.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	gender_var_update = StringVar(frm_ent_data_update)
	
	lbl_gender_update = Label(frm_ent_data_update, text = "Employee\'s Gender: ", font = ("Product Sans", 10))
	lbl_gender_update.grid(row = 3, column = 0, padx = 10, pady = 10)
	ent_gender_update = Frame(frm_ent_data_update)
	ent_gender_update.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	ent_gender_update_male = Radiobutton(ent_gender_update, indicatoron = 1, text = "   Male   ", variable = gender_var_update, value = 'M', font = ("Product Sans", 10))
	ent_gender_update_male.pack(anchor = W, fill = X)
    
	ent_gender_update_female = Radiobutton(ent_gender_update, indicatoron = 1, text = "   Female   ", variable = gender_var_update, value = 'F', font = ("Product Sans", 10))
	ent_gender_update_female.pack(anchor = W ,fill = X)
	
	lbl_salary_update = Label(frm_ent_data_update, text = "Employee\'s Salary: ", font = ("Product Sans", 10))
	lbl_salary_update.grid(row = 4, column = 0, padx = 10, pady = 10)
	ent_salary_update = Entry(frm_ent_data_update, font = ("Product Sans", 10))
	ent_salary_update.grid(row = 4, column = 1, padx = 10, pady = 10)
	
	lbl_mobile_update = Label(frm_ent_data_update, text = "Employee\'s Mobile No: ", font = ("Product Sans", 10))
	lbl_mobile_update.grid(row = 5, column = 0, padx = 10, pady = 10)
	ent_mobile_update = Entry(frm_ent_data_update, font = ("Product Sans", 10))
	ent_mobile_update.grid(row = 5, column = 1, padx = 10, pady = 10)
	
	btn_close_update = Button(frm_buttons,text = "Close", width = 12, command = win_update_employee.destroy, font = ("Product Sans", 10))
	btn_close_update.grid(row = 0, column = 0, padx = 100, pady = 10)
	
	btn_submit_update = Button(frm_buttons, text = "Update", width = 12, command = update_employee, font = ("Product Sans", 10))
	btn_submit_update.grid(row = 0, column = 1, padx = 100, pady = 10)

	
	cursor.execute("select * from employee where empid = {}".format(empid_ent_for_update.get()))
	data_to_insert = cursor.fetchall()
	
	ent_empid_update['text'] = data_to_insert[0][0]
	ent_name_update.insert(0, data_to_insert[0][1])
	ent_post_update.insert(0, data_to_insert[0][2])
	if data_to_insert[0][3] == 'M':
		ent_gender_update_male.select()
	else:
		ent_gender_update_female.select()
	
	ent_salary_update.insert(0, data_to_insert[0][4])
	ent_mobile_update.insert(0, data_to_insert[0][5])
	

	
	
	win_update_employee.mainloop()

def check_empid_for_update():
	if empid_ent_for_update.get() == "":
		mb.showerror("Employee Management", "Please Enter Employee ID")
	else:
		cursor.execute("select empid from employee")
		test_data = cursor.fetchall()
		for x in test_data:
			if x[0] == int(empid_ent_for_update.get()):
				update_employee_win()
				break
		else:
			mb.showerror("Employee Management", "No Employee with Roll No {}!".format(empid_ent_for_update.get()))

def update_employee_win_root():
	global empid_ent_for_update, temp_ent_empid_win
	temp_ent_empid_win = Tk()
	temp_ent_empid_win.title("Enter Employee ID")
	f1 = Frame(temp_ent_empid_win)
	f1.pack()
	Label(f1, text = "Enter Emp. ID: ", font = ("Product Sans", 10)).grid(row = 0 ,column = 0, padx = 20, pady = 20)
	empid_ent_for_update = Entry(f1, font = ("Product Sans", 10))
	empid_ent_for_update.grid(row = 0, column = 1, padx = 20, pady = 20)
	
	Button(temp_ent_empid_win, text = "   Continue   ", command = check_empid_for_update, font = ("Product Sans", 10)).pack(pady = 30)
	
	temp_ent_empid_win.mainloop()

def get_employee_details_del():
	employee_details_data_area.configure(state ='normal')
	employee_details_data_area.delete(1.0, END)
	
	empid_to_delete = int(ent_empid_delete.get())
	list_of_details = []
	query = "select * from employee where empid = {}".format(empid_to_delete)
	cursor.execute(query)
	raw_data = cursor.fetchall()
	try:
		loop_var = raw_data[0]
		for x in loop_var:
			list_of_details.append(x)

	
	
		data = """
***********************************
 E M P L O Y E E     D E T A I L S
***********************************

Emp. ID   : {} 
Name      : {}
Post      : {}
Gender    : {}
Salary    : {}
Mobile No : {}

***********************************
		""".format(*list_of_details)
		employee_details_data_area.insert(1.0, data)
		employee_details_data_area.configure(state ='disabled')
		btn_delete_employee['state'] = NORMAL
	except IndexError:
		mb.showerror("Employee Management", "No Employee With Emp. ID {} Found!!!".format(ent_empid_delete.get()))
	

def delete_employee():
	bool_var = mb.askyesno("Employee Management", "Do You Really Wan\'t To Delete Data Of \n Employee {}?".format(ent_empid_delete.get()))
	if bool_var:
                
		cursor.execute("delete from employee where empid = {}".format(ent_empid_delete.get()))
		mb.showinfo("Employee Management", "Employee {} deleted Successfully!".format(ent_empid_delete.get()))
		con.commit()
		win_delete_employee.destroy()
	else:
		win_delete_employee.destroy()
	

def delete_employee_win():
    global btn_delete_employee
    global employee_details_data_area
    global ent_empid_delete
    global win_delete_employee
    win_delete_employee = Tk()
    win_delete_employee.title("Delete A Employee")
    f1 = Frame(win_delete_employee)
    f1.pack(padx = 10, ipady = 30)
    
    f2 = Frame(win_delete_employee)
    f2.pack(padx = 10, ipady = 30)
    
    f3 = Frame(win_delete_employee)
    f3.pack(padx = 10, ipady = 30)
    
    Label(f1, text = "Enter Emp. ID: ", font = ("Product Sans", 10)).grid(row = 0, column = 0, padx = 10, pady = 10)
    ent_empid_delete = Entry(f1, font = ("Product Sans", 10))
    ent_empid_delete.grid(row = 0, column = 1 ,padx = 10, pady = 10)
    Button(f2, text = "Get Data", command = get_employee_details_del, font = ("Product Sans", 10)).pack(padx = 10, pady = 10)
    
    employee_details_data_area = st.ScrolledText(f2,
                                font = ('Ubuntu Mono', 10),
                                width = 35,
                                height = 12,
                                foreground = "red")
    employee_details_data_area.pack(padx = 40, pady = 20)
    employee_details_data_area.configure(state ='disabled')
    btn_delete_employee = Button(f3, text = "Delete This Employee", command = delete_employee, font = ("Product Sans", 10))
    btn_delete_employee.pack()
    btn_delete_employee['state']= DISABLED
    
    win_delete_employee.mainloop()



def show_employees():
    cursor.execute('select * from employee')
    data = cursor.fetchall()
    count = cursor.rowcount
    
    win_show_employees = Tk()
    win_show_employees.title("All Employees")
        
    cols = ["EMP. ID", "NAME", "POST", "GENDER", "SALARY", "MOBILE NO"]
    for c in range(6):
    	Label(win_show_employees, text=cols[c], font=("LEMON MILK", 10, "bold")).grid(row=0, column=c, padx=8, pady = 15)
    for x in range(count):
    	for y in range(6):
    		l = Label(win_show_employees, text = data[x][y], font = ("Product Sans", 10))
    		l.grid(row = x+1, column = y, padx = 8, pady = 7, sticky = W, ipadx = 40)
    
    
    win_show_employees.mainloop()


def add_employee():
        try:
                if (ent_empid_add.get() == "" or ent_name_add.get() == "" or ent_post_add.get() == "" or gender_var.get() == "" or ent_salary_add.get() == "" or ent_mobile_add.get() == ""):
                        mb.showerror("Employee Management", "All Fields Require At Least One Value")
                else:
                        cursor.execute("select empid from employee")
                        raw_data_roll = cursor.fetchall()
                        for x in raw_data_roll:
                                if x[0] == int(ent_empid_add.get()):
                                        mb.showerror("Employee Management", "Employee {} Already Exists!".format(ent_empid_add.get()))
                        else:
                                add_employee_query = "insert into employee values({}, '{}', '{}', '{}', {}, '{}')".format(ent_empid_add.get(), ent_name_add.get(), ent_post_add.get(), gender_var.get(), ent_salary_add.get(), ent_mobile_add.get())
                                cursor.execute(add_employee_query)
                                con.commit()
                                mb.showinfo("Employee Management", "Employee Added Successfully!")
                                win_add_employee.destroy()
        except:
                mb.showerror("Employee Management", "Enter Valid Details!")
                

def clr_employee():
	ent_empid_add.delete(0, END)
	ent_name_add.delete(0, END)
	ent_post_add.delete(0, END)
	ent_salary_add.delete(0, END)
	ent_gender_add_male.deselect()
	ent_gender_add_female.deselect()
	ent_mobile_add.delete(0, END)

def add_employee_win():
	global ent_gender_add_male
	global ent_gender_add_female
	global ent_empid_add
	global ent_name_add
	global ent_post_add
	global ent_salary_add
	global ent_mobile_add
	global gender_var
	global win_add_employee
	
	win_add_employee = Tk()
	win_add_employee.title("Add A Employee")
	win_add_employee.option_add('*Font','MiClock\ ExtraLight 8')
	
	frm_ent_data = LabelFrame(win_add_employee, text = "Enter Details",font = ("Product Sans", 10))
	frm_ent_data.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	frm_buttons = Frame(win_add_employee)
	frm_buttons.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	lbl_rollno_add = Label(frm_ent_data, text = "Enter Employee ID: ",font = ("Product Sans", 10))
	lbl_rollno_add.grid(row = 0, column = 0, padx = 10, pady = 10)
	ent_empid_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	ent_empid_add.grid(row = 0, column = 1, padx = 10, pady = 10)
	
	lbl_name_add = Label(frm_ent_data, text = "Enter Name: ",font = ("Product Sans", 10))
	lbl_name_add.grid(row = 1, column = 0, padx = 10, pady = 10)
	ent_name_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	ent_name_add.grid(row = 1, column = 1, padx = 10, pady = 10)
	
	lbl_class_add = Label(frm_ent_data, text = "Enter Post: ",font = ("Product Sans", 10))
	lbl_class_add.grid(row = 2, column = 0, padx = 10, pady = 10)
	ent_post_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	ent_post_add.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	gender_var = StringVar(frm_ent_data)
	
	lbl_gender_add = Label(frm_ent_data, text = "Enter Gender: ",font = ("Product Sans", 10))
	lbl_gender_add.grid(row = 3, column = 0, padx = 10, pady = 10)
	ent_gender_add = Frame(frm_ent_data) 
	ent_gender_add.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	ent_gender_add_male = Radiobutton(ent_gender_add, text = "Male", variable = gender_var, value = 'M',font = ("Product Sans", 10))
	ent_gender_add_male.pack(anchor = W)
    
	ent_gender_add_female = Radiobutton(ent_gender_add, text = "Female", variable = gender_var, value = 'F',font = ("Product Sans", 10))
	ent_gender_add_female.pack(anchor = W)
	
	lbl_salary_add = Label(frm_ent_data, text = "Enter Salary: ",font = ("Product Sans", 10))
	lbl_salary_add.grid(row = 4, column = 0, padx = 10, pady = 10)
	ent_salary_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	ent_salary_add.grid(row = 4, column = 1, padx = 10, pady = 10)

	lbl_mobile_add = Label(frm_ent_data, text = "Enter Mobile No: ",font = ("Product Sans", 10))
	lbl_mobile_add.grid(row = 5, column = 0, padx = 10, pady = 10)
	ent_mobile_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	ent_mobile_add.grid(row = 5, column = 1, padx = 10, pady = 10)
	
	btn_clear_add = Button(frm_buttons,text = "Clear", width = 12, command = clr_employee,font = ("Product Sans", 10))
	btn_clear_add.grid(row = 0, column = 0, padx = 100, pady = 10)
	
	btn_submit_add = Button(frm_buttons, text = "Submit", width = 12, command = add_employee,font = ("Product Sans", 10))
	btn_submit_add.grid(row = 0, column = 1, padx = 100, pady = 10)
	
	win_add_employee.mainloop()

##########################################

con = sql.connect(host = "localhost",
			      user = "",
			      passwd = "",
			      database = "test",
				  charset = 'utf8')

cursor = con.cursor()


root = Tk()
root.geometry('800x600')
root.title("Employee Management System")


Label(root,
         text = "J. N. V. Ratibad, Bhopal (M. P.)",
         font = ("LEMON MILK", 30, "bold"),
         foreground = "royalblue").pack()

Label(root, text = "Computer Science Project - Employee Management System",font = ("Product Sans", 17, "bold"), fg = "#ff6a00").pack(pady = 40)


frm_main = Frame(root)
frm_main.pack(pady = 30)

frm_main_menu = LabelFrame(frm_main, text = "Members", font = ("Product Sans", 10))
frm_main_menu.grid(row = 0, column = 0, padx = 20, pady = 20, ipadx = 20, ipady = 20)



btn_add_employee = Button(frm_main_menu, text = "Add New Employee", width = 22, bd = 3, command = add_employee_win, font = ("Product Sans", 10))
btn_add_employee.grid(row = 0, column = 0 ,padx = 10, pady = 10)

btn_show_employee = Button(frm_main_menu, text = "Show All Employees", width = 22, bd = 3, command = show_employees, font = ("Product Sans", 10))
btn_show_employee.grid(row = 0, column = 1 ,padx = 10, pady = 10)

btn_update_employee = Button(frm_main_menu, text = "Update Employee Details", width = 22, bd = 3, command = update_employee_win_root, font = ("Product Sans", 10))
btn_update_employee.grid(row = 1, column = 0 ,padx = 10, pady = 10)

btn_delete_employee = Button(frm_main_menu, text = "Delete A Employee", width = 22, bd = 3, command = delete_employee_win, font = ("Product Sans", 10))
btn_delete_employee.grid(row = 1, column = 1 ,padx = 10, pady = 10)

btn_exit_employee = Button(frm_main_menu, text = "Exit", width = 22, bg = 'red', fg = 'white', bd = 3, command = root.destroy, font = ("Product Sans", 10))
btn_exit_employee.grid(row = 2, column = 0, padx = 10, pady = 10)

root.mainloop()
