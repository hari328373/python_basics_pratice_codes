# map() function :
# For every element present in the given sequence, apply some functionality and generate
# new element with the required modification

# Without lambda:
l = [1, 2, 3, 4, 5]
def doubleIt(x):
    return 2*x
l1 = list(map(doubleIt, l))
print("apply map function without lambda : ", l1)

# with lambda:-
l = [1, 2, 3, 4, 5]
l1 = list(map(lambda x: 2*x, l))
print("apply map with lambda function : ", l1)
