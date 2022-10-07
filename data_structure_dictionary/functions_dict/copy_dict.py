#copy( )--> To create exactly duplicate dictionary (cloned copy)
d={100:"durga",200:"ravi",300:"shiva"}
d1=d.copy()
print(d1)

d1[400]="john" # the changes won't reflect to original one
print(d1)
print(d)