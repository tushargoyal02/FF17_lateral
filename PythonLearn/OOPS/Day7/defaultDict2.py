from collections import defaultdict

def func():
    return "hello"

d = defaultdict(func)



d["user"]="tushar"
d["age"]=60

#
def func2():
    return "hey"

d = defaultdict(func2)
print(d)