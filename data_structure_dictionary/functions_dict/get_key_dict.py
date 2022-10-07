#get()-->To get the value associated with the key
d={100:"john",101:"james",103:"tina",104:"tony",105:"sony",106:"james"}
print(d.get(100))

#d.get(key)-->If the key is available then returns the corresponding value
# otherwise returns None.It won't raise any error
d={100:"john",101:"james",102:"vinni",103:"tina",104:"tony",105:"sony",106:"james"}
print(d.get(107))
print(d.get(103))

#d.get(key,defaultvalue)-->If the key is available then returns the corresponding value
# otherwise returns default value
d={100:"john",101:"james",102:"vinni",103:"tina",104:"tony",105:"sony",106:"james"}
print(d.get(105,"guest"))
print(d.get(108,"guest"))