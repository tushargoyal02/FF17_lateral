from collections import Counter

# c=Counter(["A","b","c","c","A","A"])
dict1 = {"A":3,"B":2}


c=Counter(dict1)

c.update({"A":5})

# c=Counter( {"A":4})

print(type(c))
print(c)


myList=[10,20,30,10,10,20]

counterList = Counter(myList)
# counterList.update([10,20,10])

counterList.subtract([10,20,10])
print("Counter",counterList)

