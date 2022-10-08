#local variables --> The variables which are declared inside a function
# local variables are available only for the function in which we declared
# i.e. from outside of function we cannot access

def f1():
    a = 10  # local variable
    print("Accessing in f1 :",a)

def f2():
    print("Accessing in f2 :",a) # returns NameError


f1()
f2()
print("Accessing outside function",a)  # returns NameError