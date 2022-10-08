x = 5  # initializing a global variable
def f1():  # defining a function
    x = 4  # initializing a local variable
    print("local x:", x)

f1()
print("global x:", x)

def f2():
    print("x value in f2:", x)
f2()

# the global value print in inside function

a = 10  #global variable
def f1():
    a = 777  #local variable
    print("local variable a:",a)
    print("global variable inside function",globals()['a'])
# The inbuilt function globals( )[str] converts the string 'str' into a class name and returns the class name

f1()
print("global variable outside function",a)