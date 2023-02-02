import sqlite3

con = sqlite3.connect("job.db")
program_cursor = con.cursor() #Reading line by line



def check_department(dept_id):
  #sql query
  sql_query = 'select * from department_data where dept_id=?'

  num_rows = 0
  for row in program_cursor.execute(sql_query, [dept_id]):
    # print(row)
    num_rows += 1
  
  #Returns boolean value, if dept exist = True
  #num_rows = program_cursor.rowcount
  #print(num_rows)

  if num_rows >= 1:
    return True
  else: 
    return False



def insert_department():
  
  while True:
    try:
        department_id = int(input("Enter the department ID: "))
        break
    except ValueError:
        print("Must be a number")
  

  if check_department(department_id):
    print("Sorry that department id is already entered ")
  else:
    department_name = input("Enter the department name: ")
    department_budget = int(input("Enter the department budget: "))
    department_man = input("Enter the department manager: ")
    data = (department_id, department_name, department_budget, department_man)

    #insert into database
    sql_query = 'insert into department_data values(?, ?, ?, ?)'
    program_cursor = con.cursor()
    program_cursor.execute(sql_query, data)
    con.commit()

    print("Department added")


def update_department():
  while True:
    try:
        department_id = int(input("Enter the department ID: "))
        break
    except ValueError:
        print("Must be a number")

  if not check_department(department_id):
    print("Sorry that department does not exist ")

  else:
    while True:
      try: category = int(input("Enter the category you want to modify \n \
      (1 - name, 2 - budget, 3 - manager): "))
      except ValueError as e: print(e)
      else:
      
        if category == 1:
          selection = input("Enter the new name: ")
          sql_query = 'select dept_name from department_data where dept_id = ?'
          data = (department_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update department_data set dept_name = ? where dept_id = ?'
          data1 = (selection, department_id)
          program_cursor.execute(sql_query1, data1)
          con.commit()
          
        if category == 2:
          selection = int(input("Enter the new budget: "))
          sql_query = 'select dept_budget from department_data where dept_id = ?'
          data = (department_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update department_data set dept_budget = ? where dept_id = ?'
          data1 = (selection, department_id)
          program_cursor.execute(sql_query1, data1)
          con.commit()
          
        """if category == 3:
          selection = input("Enter the new department: ")
          sql_query = 'select emp_dept from employee_data where emp_id = ?'
          data = (department_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update employee_data set emp_dept = ? where emp_id = ?'
          data1 = (selection, department_id)
          program_cursor.execute(sql_query1, data1)"""
          
        if category == 3:
          selection = input("Enter the new manager: ")
          sql_query = 'select dept_man from department_data where dept_id = ?'
          data = (department_id,)
          program_cursor = con.cursor()  
          program_cursor.execute(sql_query, data)
          sql_query1 = 'update department_data set dept_man = ? where dept_id = ?'
          data1 = (selection, department_id)
          program_cursor.execute(sql_query1, data1)  
          con.commit()
    
    
        print("Employee updated")
        break



def remove_department():
  while True:
    try:
        department_id = int(input("Enter the employee ID: "))
        break
    except ValueError:
        print("Must be a number")

  if not check_department(department_id):
    print("Sorry that department does not exist ")

  else:
    sql_query = 'select dept_name from department_data where dept_id = ?'
    data = (department_id,)

    program_cursor = con.cursor()  
    program_cursor.execute(sql_query, data)

    fetch_department_name = program_cursor.fetchone()
    if fetch_department_name == []:
        print("No department by that name")
      
    confirmation = input(f"Are you sure you want to remove this department {fetch_department_name}? (y/n)")

    if confirmation == 'y' or 'Y':
      sql_query1 = 'delete from department_data where dept_id = ?'
      data1 = (department_id,)
      program_cursor = con.cursor()  
      program_cursor.execute(sql_query1, data1)
      con.commit()

      print("Department removed")



def check_all_departments():
  sql_query = 'select * from department_data'

  program_cursor = con.cursor()  
  program_cursor.execute(sql_query)

  fetch_department = program_cursor.fetchall()
  if fetch_department == []:
        print("No department by that name")
  for i in fetch_department:
    print('--------------------')
    print("Department ID: ", i[0])
    print("Department name: ", i[1])
    print("Department budget: ", i[2])
    print("Department manager: ", i[3])
    print('--------------------\n')


def check_departments_cate():
  while True:
    
    try: 
      category = int(input("Enter a category (1 - id, 2 - budget, 3 - manager) : "))
      rank = input("Ascending order or descending? (a/d)")
    except ValueError as e: print(e)
    else:
  
      if int(category) <= 0 and int(category) >= 4:
        print("Sorry that category doesn't exist")
      else:
        #ID
        if category == 1 and rank == 'a':
          sql_query = 'select * from department_data order by dept_id'
          program_cursor.execute(sql_query)
        if category == 1 and rank == 'd':
          sql_query = 'select * from department_data order by dept_id desc'
          program_cursor.execute(sql_query)
    
        #Budget
        if category == 2 and rank == 'a':
          sql_query = 'select * from department_data order by dept_budget'
          program_cursor.execute(sql_query)
        if category == 2 and rank == 'd':
          sql_query = 'select * from department_data order by dept_budget desc'  
          program_cursor.execute(sql_query)
          
        #Manager
        if category == 3 and rank == 'a':
          sql_query = 'select * from department_data order by dept_man'
          program_cursor.execute(sql_query)
        if category == 3 and rank == 'd':
          sql_query = 'select * from department_data order by dept_man desc'
          program_cursor.execute(sql_query)
      
      result = program_cursor.fetchall()
      if result == []:
        print("No department in that category")
      for i in result:
        print('--------------------')
        print("Department ID: ", i[0])
        print("Department name: ", i[1])
        print("Department budget: ", i[2])
        print("Department manager: ", i[3])
        print('--------------------\n')
      break
    

# def check_department_range():
#   #assuming ids for employees are sequential, i.e. first employee would be 1, etc
#   while True:
#     try:
#       category = int(input("Enter a category (1 - id, 2 - budget) : "))
#       lower_value = int(input("Enter the lower value of the range you want to search: "))
#       upper_value = int(input("Enter the upper value of the range you want to search: "))

#       if category == 2: 
#         int(lower_value)
#         int(upper_value)
        
#     except ValueError as e: print(e)
#     else:
      
#       if category == 1:
#         sql_query = "select * from employee_data where emp_id between ? and ?"
#         data = (lower_value, upper_value)
#         program_cursor.execute(sql_query, data)
#       if category == 2:
#         sql_query = "select * from employee_data where emp_salary between ? and ?"
#         data = (lower_value, upper_value)
#         program_cursor.execute(sql_query, data)
    
    
#       fetch_employee = program_cursor.fetchall()
#       for i in fetch_employee:
#         print('--------------------')
#         print("Employee ID: ", i[0])
#         print("Employee name: ", i[1])
#         print("Employee salary: ", i[2])
#         print("Employee department: ", i[3])
#         print("Employee manager: ", i[4])
#         print('--------------------\n')  
#       break
  

def department_search():
  while True:
    try: dept_num = int(input("Search for an department using id or name (1 - ID, 2 - name): "))
    except ValueError as e: print(e)
    else:
  
      if dept_num == 1:
        selection = input("What is the department ID?")
        sql_query = "select * from department_data where dept_id = ?"
        data = ([selection])
        program_cursor.execute(sql_query, data)
      if dept_num == 2:
        selection = input("What is the department name?")
        sql_query = "select * from department_data where dept_name = ?"
        data = ([selection])
        program_cursor.execute(sql_query, data)
    
      fetch_dept = program_cursor.fetchall()
      if fetch_dept == []:
        print("No department by that ID/name")
      for i in fetch_dept:
        print('--------------------')
        print("Department ID: ", i[0])
        print("Department name: ", i[1])
        print("Department budget: ", i[2])
        print("Department manager: ", i[3])
        print('--------------------\n')

      break
  

def check_manager():
  manager = input("Enter the manager: ")
  sql_query = "select * from department_data where dept_man = ?"

  program_cursor = con.cursor()
  program_cursor.execute(sql_query, [manager])

  print(f"Departments under {manager}")
  fetch_dept = program_cursor.fetchall()
  if fetch_dept == []:
        print("No manager by that name")
  for i in fetch_dept:
    print('--------------------')
    print("Department ID: ", i[0])
    print("Department name: ", i[1])
    print("Department budget: ", i[2])
    print("Department manager: ", i[3])
    print('--------------------\n')


def check_employee_in_department():
  department = input("Enter the department: ")

  """"SELECT table1.column1, table1.column2,table2.column1,....
FROM table1 
INNER JOIN table2
ON table1.matching_column = table2.matching_column;

  program_cursor.execute("CREATE TABLE employee_data (emp_id int(11) primary key, \
  emp_name var(50), emp_salary int, emp_dept var(50), emp_man var(50))")
  print("EMPLOYEE MANAGEMENT SYSTEM")
  program_cursor.execute("CREATE TABLE department_data (dept_id int(11) primary key, dept_name var(50), \
  dept_budget int, dept_man var(50))")"""

  sql_query = "select * from employee_data join department_data on \
  employee_data.emp_dept = ?"

  program_cursor = con.cursor()
  program_cursor.execute(sql_query, [department])

  print(f"Employees under {department}")
  fetch_employee = program_cursor.fetchall()
  if fetch_employee == []:
        print("No employee by that name in this department")
  for i in fetch_employee:
    print(i)
    print('--------------------')
    print("Employee ID: ", i[0])
    print("Employee name: ", i[1])
    print("Employee salary: ", i[2])
    print("Employee department: ", i[3])
    print("Employee manager: ", i[4])
    print('--------------------\n')





class RangeError(Exception): pass

def department_menu():
  print("DEPARTMENT MANAGEMENT SYSTEM")
  option = 0
  while option != 9:
    try: 
      print("""Department Menu
      ------------
      1. Add Department
      2. Update Department
      3. Delete Department
      4. List All Department
      5. List Department By Category (ascending or descending)
      6. Department Search
      7. Employees Within Department Search
      8. Manager Search
      9. Exit to main menu
      ------------""")
      option = int(input("Please select an option: "))

      if 0 > option > 9: raise RangeError("Option Out Of Bounds")
    except ValueError as e: print(e)
    except RangeError as e: print(e)
    else:
      if option == 1: insert_department()
      if option == 2: update_department()
      if option == 3: remove_department()
      if option == 4: check_all_departments()
      if option == 5: check_departments_cate()
      if option == 6: department_search()
      if option == 7: check_employee_in_department()
      if option == 8: check_manager()        
      #if option == ##: 
