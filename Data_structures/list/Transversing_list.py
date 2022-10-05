#The sequential access of each element in the list.

#by using while loop
n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1

#by using for loop
l=[0,"abc",False,2.5,40,25,8]
for n in l:
    print(n)

#display even numbers
for i in range(0,21):
    if i%2==0:
        print(i)


