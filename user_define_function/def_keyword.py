# user define function code with "def"keyword

# function to check whether the given number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even Number")
    else:
        print(num, "is Odd Number")


even_odd(10)
even_odd(15)

# function to find factorial of given number?
def fact(num):
    result = 1
    while num >= 1:
        result = result*num
        num = num-1
    return result


for i in range(1, 5):
    print("The Factorial of", i, "is :", fact(i))
