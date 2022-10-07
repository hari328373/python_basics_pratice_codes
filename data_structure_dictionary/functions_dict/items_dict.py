#items()--> It returns list of tuples representing key-value pairs
# [(k,v),(k,v),(k,v)]
d={100:"durga",200:"ravi",300:"shiva"}
print(d.items())

for k,v in d.items():
    print(k,"--",v)