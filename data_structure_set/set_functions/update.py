# update(x,y,z)-->To add multiple items to the set
# Arguments are Iterable objects like List,range etc

s = {10, 20, 30}
l = [40, 50, 60, 10]
s.update(l, range(5))
print(s)
