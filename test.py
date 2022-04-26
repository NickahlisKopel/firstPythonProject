import array

print("Hello Test")

# if __name__ == '__main__':
#     print("name is main")
# else:
#     print("name is not main")
careerdevs = ["Gabriel", "Margie", "Cliff", "Arnell"]

accept = input("Do you work for CareerDevs?\n(yes/no): ")

if accept == "yes":
    name = input("What is your name?: ")
    for emp_name in careerdevs:
        if name == emp_name:
            print("Okay, you're an employee")
        else:
            print("You're not an employee")
else:
    print("Okay, you can leave")


#Recreate for student

