# In dictionary, index are not allowed for access the elements
# for accessing keys are used
#when key are accessed then return corresponding  value  of that key
d={100:"john",101:"james",103:"tina",104:"tony",105:"sony"}
print(d[100])
print(d[105])
#print(d[106]) #If the specified key is not available then we will get Key Error

# keys duplicates are not allowed but values can be duplicated
# if keys are duplicate then old value is replace with new one
d={100:"john",101:"james",103:"tina",104:"tony",105:"sony",100:"rames"}
print(d)
#values can duplicate
d={100:"john",101:"james",103:"tina",104:"tony",105:"sony",106:"james"}
print(d)