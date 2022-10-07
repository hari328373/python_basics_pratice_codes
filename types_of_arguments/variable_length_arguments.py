# pass variable number of arguments to our function
# declare a variable length argument with * symbol --> def f1(*n)
# call this function by passing any number of arguments including zero number

def sum(*n):
    total = 0
    for n1 in n:
        total = total+n1
    print("The Sum=", total)


sum()
sum(10)
sum(10, 20)
sum(10, 20, 30, 40)
