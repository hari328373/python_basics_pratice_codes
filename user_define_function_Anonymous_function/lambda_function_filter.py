# filter() function to filter values from the given sequence based on some condition

# without lambda Function:
def iseven(x):
    if x % 2 == 0:
        return True
    else:
        return False
l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(iseven, l))
print("filter values without lambda function: ", l1)

# with lambda Function:
l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(lambda x: x % 2 == 0, l))
print("filter even values with lambda function: ", l1)
l2 = list(filter(lambda x: x % 2 != 0, l))
print("filter odd values with lambda function: ", l2)
