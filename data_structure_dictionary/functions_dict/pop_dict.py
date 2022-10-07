#pop()-->It removes the entry associated with the specified key and returns the corresponding value
d={100:"john",101:"james",102:"vinni",103:"tina",104:"tony",105:"sony",106:"james"}
print(d.pop(102))
print(d)

#popitem()-->it removes an arbitrary item (k-v pair) and return it
d={100:"john",101:"james",102:"vinni",103:"tina",104:"tony",105:"sony",106:"james"}
print(d.popitem())
print(d.popitem())
print(d)
#If the dictionary is empty then we will get KeyError
d1=dict()
print(d1.popitem())