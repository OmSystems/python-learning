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
address = '123 Main Street'
address += ', Apartment 4B'

# Combining strings and integers
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Experience info
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# F-string formatting
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# String slicing
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)
