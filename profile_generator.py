"""
Employee Profile Generator
------------------------------
It is used to generate an employee profile on the basis of info of the employee
like -- name, age, address, experience, etc.
"""

first_name = 'John'
last_name = 'Doe'

full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'

employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analytics'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Positon: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)

last_three = employee_code[-3:]
print(last_three)