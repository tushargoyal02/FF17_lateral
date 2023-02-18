

#  Iterable => object where we can run a for loop
#  __iter__ method



#  Iterator : object which implement iterable protocol
#  each element one by one ( __next__())
data="tushar"

listData = dir(data)



#  iter method
iterString =  data.__iter__()
print(iterString)

print(next(iterString))
print(next(iterString))
# print("__next__" in listData)

# for var in data:
#     print(var)