# ============================================
# Python Basics - Strings
# FreeCodeCamp Python Course
# Author: Om Patel
# ============================================

# Basic string concatenation
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

# String with += operator
home_address = '123 Main Street'
home_address += ', Apartment 4B'

# Combining strings and integers
emp_age = 28
emp_info = full_name + ' is ' + str(emp_age) + ' years old'
print(emp_info)

# Experience info
exp_years = 5
exp_info = 'Experience: ' + str(exp_years) + ' years'
print(exp_info)

# F-string formatting
job_position = 'Data Analyst'
annual_salary = 75000
emp_card = f'Employee: {full_name} | Age: {emp_age} | Position: {job_position} | Salary: ${annual_salary}'
print(emp_card)

# String slicing
emp_code = 'DEV-2026-JD-001'
dept_code = emp_code[0:3]
print(dept_code)

year_part = emp_code[4:8]
print(year_part)

init_part = emp_code[9:11]
print(init_part)
