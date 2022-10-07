# arguments passed to function in correct positional order
# If we change the order then result may be changed

def sub(a, b): # a,b are formal Arguments
    print(a - b)


sub(100, 200) # here the values 100,200 are Actual Arguments
sub(200, 100)
