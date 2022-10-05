#pop-->It removes and returns the last element of the list

n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n)

# n.pop(index)===>To remove and return element present at specified index
n=[10,20,30,40,50,60]
print(n.pop())
print(n.pop(1))
print(n.pop(10)) #IndexError: pop index out of range