import department
import employee
import sqlite3

con = sqlite3.connect("job.db")
program_cursor = con.cursor()

class RangeError(Exception): pass


def main():
  program_cursor.execute("drop table if exists employee_data")
  program_cursor.execute("drop table if exists department_data ")

  program_cursor.execute("CREATE TABLE employee_data (emp_id int(11) primary key, \
  emp_name var(50), emp_salary int, emp_dept var(50), emp_man var(50))")
  print("EMPLOYEE MANAGEMENT SYSTEM")
  program_cursor.execute("CREATE TABLE department_data (dept_id int(11) primary key, dept_name var(50), \
  dept_budget int, dept_man var(50))")
  
  database_cycle = True
  while database_cycle:
    try: 
      database_selection = int(input("Which database do you want to start with? (1 - employee, 2 - department, 3 - Exit):"))
      if 0 > database_selection > 2: raise RangeError("Option Out Of Bounds")
    except ValueError as e: print(e)
    else:
      
      if database_selection == 1: employee.employee_init()
      if database_selection == 2: department.department_menu()
      if database_selection == 3: database_cycle = False

    

if __name__ == '__main__': main()
