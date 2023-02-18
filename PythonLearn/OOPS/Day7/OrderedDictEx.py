from collections import OrderedDict


o =OrderedDict()

o["user"]="Tushar"
o["age"]=10011
o["salary"]=99

print(o)

o.move_to_end("salary",last=False)



print(o)

o.popitem(last=False)
print("After Popitem",o)

