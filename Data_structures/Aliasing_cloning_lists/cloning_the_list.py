#The process of creating exactly duplicate independent object
#cloning by using slicing
x=[10,20,30,40]
y=x[:]
y[1]=777
print(x) # modifications won't reflect
print(y)

a=[1,2,3,4]
b=a[:3]
print(a)
print(b)

#by using copy function
p=[1,2,3,4]
q=p.copy()
q[1]=999
print(p)
print(q)