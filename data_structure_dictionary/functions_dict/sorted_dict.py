#sorted-->For numbers ==>default natural sorting order is Ascending Order
#For Strings ==> default natural sorting order is Alphabetical Order

#sorted items in form of list of tuples
d={20:"abc",30:50,10:5,9:"xyz",4:"pqr",6:5,70:3}
print(sorted(d.items()))

#sorted keys and returns  in form of list
d={20:"abc",30:50,10:5,9:"xyz",4:"pqr",6:5,70:3}
print(sorted(d.keys()))

#sorted values and return in form of  list
d={20:"abc",30:"out",10:"aws",9:"xyz",4:"pqr",6:"pop",70:"cut"}
print(sorted(d.values()))