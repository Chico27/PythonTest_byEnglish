
employee_file = open("employees.txt", "r")

print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

employee_file.close()

employee_file = open("employees.txt", "r")

print(employee_file.readlines())

employee_file.close()
employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()




