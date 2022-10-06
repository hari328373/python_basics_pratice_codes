#access either by index or by slice operator

#by index
t=(10,20,30,40,50,60)
print(t[0])
print(t[-1])

#by slice operator
t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100]) # if stop value is out of range then it return elements upto last
print(t[::2])