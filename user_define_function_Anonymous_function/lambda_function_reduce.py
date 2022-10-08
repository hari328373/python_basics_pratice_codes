# reduce() function reduces sequence of elements into a single element by applying the specified function
# reduce() function present in functools module

from functools import *
l = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x+y, l)
print("reduce the values :", result)

# sum the numbers in range of 100
from functools import *
result = reduce(lambda x, y: x+y, range(1, 101))
print("reduce the values :", result)
