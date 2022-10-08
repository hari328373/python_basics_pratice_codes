# the purpose of the global keyword is:
# 1. To declare global variable inside function
# 2. To make global variable available to the function
# we can perform required modifications inside function

a = 10  # global variable declaration
def f1():
    global a # using global keyword to modify the value inside the function
    a = a + 5
    print("Accessing inside function ",a)

f1()
print("Accessing outside function ", a)
