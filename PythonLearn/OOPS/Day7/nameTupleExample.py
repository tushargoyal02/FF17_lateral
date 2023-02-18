from collections import namedtuple


data= namedtuple("data",["fnam","salary"])


print(data)
d = data("tushar",1011)
print(data)


print(d[0])

print(d.fnam)