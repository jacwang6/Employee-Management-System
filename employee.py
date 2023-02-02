import sqlite3

con = sqlite3.connect("job.db")

program_cursor = con.cursor() #Reading line by line



def check_employee(emp_id):
  #sql query
  sql_query = 'select * from employee_data where emp_id=?'

  num_rows = 0
  for row in program_cursor.execute(sql_query, [emp_id]):
    # print(row)
    num_rows += 1
  
  #Returns boolean value, if employee exist = True
  #num_rows = program_cursor.rowcount
  #print(num_rows)

  if num_rows >= 1:
    return True
  else: 
    return False


#adds new employee to database if not already in database
def insert_employee():
  
  while True:
    try:
        employee_id = int(input("Enter the employee ID: "))
        break
    except ValueError:
        print("Must be a number")
  

  if check_employee(employee_id):
    print("Sorry that employee id is already entered ")
  else:
    employee_name = input("Enter the employee's name: ")
    while True:
      try:
          employee_salary = int(input("Enter the employee's salary: "))
          break
      except ValueError:
          print("Must be a number")
    employee_dept = input("Enter the employee's department: ")
    employee_man = input("Enter the employee's manager: ")
    data = (employee_id, employee_name, employee_salary, employee_dept, employee_man)

    #insert into database
    sql_query = 'insert into employee_data values(?, ?, ?, ?, ?)'
    program_cursor = con.cursor()
    program_cursor.execute(sql_query, data)
    con.commit()
    
    print("Employee added")

#updates employee data in database, if employee is in database
def update_employee():
  while True:
    try:
        employee_id = int(input("Enter the employee ID: "))
        break
    except ValueError:
        print("Must be a number")

  if not check_employee(employee_id):
    print("Sorry that employee does not exist ")

  else:
    while True:
      try: category = int(input("Enter the category you want to modify \n \
      (1 - name, 2 - salary, 3 - department, 4 - manager): "))
      except ValueError as e: print(e)
      else:
      
        if category == 1:
          selection = input("Enter the new name: ")
          sql_query = 'select emp_name from employee_data where emp_id = ?'
          data = (employee_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update employee_data set emp_name = ? where emp_id = ?'
          data1 = (selection, employee_id)
          program_cursor.execute(sql_query1, data1)
          con.commit()
          
        if category == 2:
          selection = int(input("Enter the new salary: "))
          sql_query = 'select emp_salary from employee_data where emp_id = ?'
          data = (employee_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update employee_data set emp_salary = ? where emp_id = ?'
          data1 = (selection, employee_id)
          program_cursor.execute(sql_query1, data1)
          con.commit()
          
        if category == 3:
          selection = input("Enter the new department: ")
          sql_query = 'select emp_dept from employee_data where emp_id = ?'
          data = (employee_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          con.commit()
          sql_query1 = 'update employee_data set emp_dept = ? where emp_id = ?'
          data1 = (selection, employee_id)
          program_cursor.execute(sql_query1, data1)
          con.commit()
          
        if category == 4:
          selection = input("Enter the new manager: ")
          sql_query = 'select emp_man from employee_data where emp_id = ?'
          data = (employee_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update employee_data set emp_man = ? where emp_id = ?'
          data1 = (selection, employee_id)
          program_cursor.execute(sql_query1, data1) 
          con.commit()
    
    
        print("Employee updated")
        break


#removes employee from database, if employee is on database
def remove_employee():
  while True:
    try:
        employee_id = int(input("Enter the employee ID: "))
        break
    except ValueError:
        print("Must be a number")

  if not check_employee(employee_id):
    print("Sorry that employee does not exist ")

  else:
    sql_query = 'select emp_name from employee_data where emp_id = ?'
    data = (employee_id,)

    program_cursor = con.cursor()  
    program_cursor.execute(sql_query, data)

    fetch_employee_name = program_cursor.fetchone()
    
    confirmation = input(f"Are you sure you want to remove this employee {fetch_employee_name}? (y/n)")

    if confirmation == 'y' or 'Y':
      sql_query1 = 'delete from employee_data where emp_id = ?'
      data1 = (employee_id,)
      program_cursor = con.cursor()  
      program_cursor.execute(sql_query1, data1)
      con.commit()

      print("Employee removed")


#returns a list of all employees on database
def check_all_employees():
  sql_query = 'select * from employee_data'

  program_cursor = con.cursor()  
  program_cursor.execute(sql_query)

  fetch_employee = program_cursor.fetchall()
  if fetch_employee == []:
        print("No employees on database.")
    
  for i in fetch_employee:
    print('--------------------')
    print("Employee ID: ", i[0])
    print("Employee name: ", i[1])
    print("Employee salary: ", i[2])
    print("Employee department: ", i[3])
    print("Employee manager: ", i[4])
    print('--------------------\n')

#returns a list of employees by a chosen category
def check_employees_cate():
  while True:
    
    try: 
      category = int(input("Enter a category (1 - id, 2 - salary, 3 - department) : "))
      rank = input("Ascending order or descending? (a/d)")
    except ValueError as e: print(e)
    else:
  
      if int(category) <= 0 and int(category) >= 4:
        print("Sorry that category doesn't exist")
      else:
        #ID
        if category == 1 and rank == 'a':
          sql_query = 'select * from employee_data order by emp_id'
          program_cursor.execute(sql_query)
        if category == 1 and rank == 'd':
          sql_query = 'select * from employee_data order by emp_id desc'
          program_cursor.execute(sql_query)
    
        #Salary
        if category == 2 and rank == 'a':
          sql_query = 'select * from employee_data order by emp_salary'
          program_cursor.execute(sql_query)
        if category == 2 and rank == 'd':
          sql_query = 'select * from employee_data order by emp_salary desc'  
          program_cursor.execute(sql_query)
          
        #Department
        if category == 3 and rank == 'a':
          sql_query = 'select * from employee_data order by emp_dept'
          program_cursor.execute(sql_query)
        if category == 3 and rank == 'd':
          sql_query = 'select * from employee_data order by emp_dept desc'
          program_cursor.execute(sql_query)
      
      result = program_cursor.fetchall()
      if result == []:
        print("No employees in that category")
      for i in result:
        print('--------------------')
        print("Employee ID: ", i[0])
        print("Employee name: ", i[1])
        print("Employee salary: ", i[2])
        print("Employee department: ", i[3])
        print("Employee manager: ", i[4])
        print('--------------------\n')
      break
    
#returns a list of employees based on a given range
def check_employees_range():
  #assuming ids for employees are sequential, i.e. first employee would be 1, etc
  while True:
    try:
      category = int(input("Enter a category (1 - id, 2 - salary) : "))
      lower_value = int(input("Enter the lower value of the range you want to search: "))
      upper_value = int(input("Enter the upper value of the range you want to search: "))

      if category == 2: 
        int(lower_value)
        int(upper_value)
        
    except ValueError as e: print(e)
    else:
      
      if category == 1:
        sql_query = "select * from employee_data where emp_id between ? and ?"
        data = (lower_value, upper_value)
        program_cursor.execute(sql_query, data)
      if category == 2:
        sql_query = "select * from employee_data where emp_salary between ? and ?"
        data = (lower_value, upper_value)
        program_cursor.execute(sql_query, data)
    
    
      fetch_employee = program_cursor.fetchall()
      if fetch_employee == []:
        print("No employees in that range")
      for i in fetch_employee:
        print('--------------------')
        print("Employee ID: ", i[0])
        print("Employee name: ", i[1])
        print("Employee salary: ", i[2])
        print("Employee department: ", i[3])
        print("Employee manager: ", i[4])
        print('--------------------\n')  
      break
  
#searches for a given 
def employee_search():
  while True:
    try: employee_num = int(input("Search for an employee using id or name (1 - ID, 2 - name): "))
    except ValueError as e: print(e)
    else:
  
      if employee_num == 1:
        selection = input("What is the employee ID?")
        sql_query = "select * from employee_data where emp_id = ?"
        data = ([selection])
        program_cursor.execute(sql_query, data)
      if employee_num == 2:
        selection = input("What is the employee name?")
        sql_query = "select * from employee_data where emp_name = ?"
        data = ([selection])
        program_cursor.execute(sql_query, data)
    
      
      fetch_employee = program_cursor.fetchall()
      if fetch_employee == []:
        print("No employees by that ID/name")
      for i in fetch_employee:
        print('--------------------')
        print("Employee ID: ", i[0])
        print("Employee name: ", i[1])
        print("Employee salary: ", i[2])
        print("Employee department: ", i[3])
        print("Employee manager: ", i[4])
        print('--------------------\n')
      break
#returns a list of employees in a given department  
def check_department():
  department = input("Enter the department: ")
  sql_query = "select * from employee_data where emp_dept = ?"

  program_cursor = con.cursor()
  program_cursor.execute(sql_query, [department])

  print(f"Employees under {department}")
  fetch_employee = program_cursor.fetchall()
  if fetch_employee == []:
        print("No employees in that department")
  for i in fetch_employee:
    print('--------------------')
    print("Employee ID: ", i[0])
    print("Employee name: ", i[1])
    print("Employee salary: ", i[2])
    print("Employee department: ", i[3])
    print("Employee manager: ", i[4])
    print('--------------------\n')

#return employees under a given manager
def check_manager():
  manager = input("Enter the manager: ")
  sql_query = "select * from employee_data where emp_man = ?"

  program_cursor = con.cursor()
  program_cursor.execute(sql_query, [manager])

  print(f"Employees under {manager}")
  fetch_employee = program_cursor.fetchall()
  if fetch_employee == []:
        print("No employees under that manager")
  for i in fetch_employee:
    print('--------------------')
    print("Employee ID: ", i[0])
    print("Employee name: ", i[1])
    print("Employee salary: ", i[2])
    print("Employee department: ", i[3])
    print("Employee manager: ", i[4])
    print('--------------------\n')

class RangeError(Exception): pass

def employee_init():

  option = 0
  while option != 10:
    try:
      print("""Main Menu
      ------------
      1. Add Employee
      2. Update Employee
      3. Delete Employee
      4. List All Employees
      5. List Employees By Category (ascending or descending)
      6. List Employees Within Range (specify category)
      7. Employee Search
      8. Department Search
      9. Manager Search
      10. Exit to main menu
      ------------""")
      option = int(input("Please select an option: "))

      if 0 > option > 9: raise RangeError("Option Out Of Bounds")
    except ValueError as e: print(e)
    except RangeError as e: print(e)
    else:
      if option == 1: insert_employee()
      if option == 2: update_employee()
      if option == 3: remove_employee()
      if option == 4: check_all_employees()
      if option == 5: check_employees_cate()
      if option == 6: check_employees_range()
      if option == 7: employee_search()
      if option == 8: check_department()
      if option == 9: check_manager()        
   
