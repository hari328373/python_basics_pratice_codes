# append() function to add item at the end of the list.

'''list=[  ]
list.append("A")
list.append("B")
list.append("C")
print(list)'''

# To add all elements to list up to 100 which are divisible by 10
l=[ ]
for i in range(101):
    if i%10==0:
        l.append(i)
print(l)