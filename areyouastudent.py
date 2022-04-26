students = ["Nick", "John", "Keith", "Brett"]

is_student = False


print("Are your a student? Lets find out...")
question = input("Are you a student?\n(yes/no): ").strip()
while question == "" or question[0] != "y" and question[0] != "n":
    question = input("Are you a student?\n(yes/no): ")
if question[0] == "y":
    name = input("What is your name?\nname: ").strip()
    for student_name in students:
        if name == student_name:
            is_student = True
    if is_student:
        print("Welcome to class.")
    else:
        print("You're not supposed to be here.")
else:
    print("Bye!")
    exit()
