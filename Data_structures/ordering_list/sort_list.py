#For numbers ==>default natural sorting order is Ascending Order
n=[20,5,15,10,0]
n.sort()
print(n)

#For Strings ==> default natural sorting order is Alphabetical Order
s=["Dog","Banana","Cat","Apple"]
s.sort()
print(s)

#sort according to reverse
l=[40,20,10,30]
l.sort()
print(l)

l.sort(reverse=True) # sort and reverse
print(l)

l.sort(reverse=False) # only sort
print(l)