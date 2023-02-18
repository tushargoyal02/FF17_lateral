
from collections import defaultdict

# list() => it take function as an argument
d = defaultdict(list)

d["A"].append(10)
d["b"].append(20)

print(d["A"], d["b"])


print(d["c"])

# myDictionary={"a":10,"B":20}

# print(myDictionary["a"])
# print(myDictionary["c"])