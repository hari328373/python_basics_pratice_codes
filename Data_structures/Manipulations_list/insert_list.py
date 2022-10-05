#To insert item at specified index position

n=[1,2,3,4,5]
n.insert(1,888) #inset 888 in first index
print(n)

p=[1,2,3,4,5]
p.insert(10,777) #If the specified index is greater than max index then element will be inserted at last position
p.insert(-10,999) #If the specified index is smaller than min index then element will be inserted at first position
print(p)
