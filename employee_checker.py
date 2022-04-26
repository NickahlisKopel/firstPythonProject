
COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

is_employee = 0

# Welcome message + employee names listed out
print("\nWelcome to the "+COMPANY_NAME+" employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- "+emp_name)
print("\n")

# user input section (buggy code)
accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
if accept == "yes":
    name = input("What is your name?\nName: ")
    for emp_name in EMPLOYEES:
        if name == emp_name:
            is_employee = is_employee + 1
    if is_employee > 0:
        print("Thank you " + name + ", you are now checked in.")
    else:
        print("You're not an employee")
else:
    print("This service is not for you. Exiting program...")
    exit()


