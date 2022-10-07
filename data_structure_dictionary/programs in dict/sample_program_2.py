# program to accept student name and marks from the keyboard and creates a dictionary
n = int(input("enter no. of students: "))
d = {}
for i in range(n):
    name = input("student name: ")
    marks = input("student marks: ")
    d[name] = marks
while True:
    name = input("enter student name to get marks: ")
    marks = d.get(name, -1)
    if marks == -1:
        print("student not found")
    else:
        print("the marks of ", name, "are", marks)
    option = input("Do you want to find another student marks [yes|no]: ")
    if option == "no":
        break
print("thanks for using our application")
