#If the key is not available then a new entry will be added
# to the dictionary with the specified key-value pair
d={100:"durga",200:"ravi",300:"shiva"}
print(d)
d[400]="pavan"
print(d)

#If the key is already available then old value will be replaced with new value
d={100:"durga",200:"ravi",300:"shiva"}
d[100]="sunny"
print(d)
