#d.setdefault(k,v)
#If the key is already available then this function returns the corresponding value
#If the key is not available then the specified key-value will be added as new item to the dictionary
d={100:"durga",200:"ravi",300:"shiva"}
print(d.setdefault(400,"pavan")) # added to dict
print(d)
print(d.setdefault(100,"sachin")) # returns corresdonding value
print(d)

