#aliasing-->The process of giving another reference variable to the existing list
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))

x=[10,20,30,40]
y=x
y[1]=777
print(x) #if we are changing content,then those changes will be reflected to the other reference variable
print(y)