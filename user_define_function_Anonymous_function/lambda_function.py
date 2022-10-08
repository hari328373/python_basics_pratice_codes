# we can declare a function without any name,
# such type of nameless functions are called anonymous functions or lambda functions
# The main purpose of anonymous function is just for instant use

#program to create a lambda function to find square of given number?
s = lambda n: n*n
print("The Square of 4 is :", s(4))
print("The Square of 5 is :", s(5))

# Lambda Function to find biggest of given values.
s = lambda a, b: a if a > b else b
print("The Biggest of 10,20 is:", s(10, 20))
print("The Biggest of 100,200 is:", s(100, 200))
