# global variables--> The variables which are declared outside of function
# These variables can be accessed in all functions of that module

a = 10  # global variable declaration
def f1():
    print("Accessing in f1 : ",a)

def f2():
    print("Accessing in f2 :",a)


f1()
f2()
print("Accessing outside the function", a)