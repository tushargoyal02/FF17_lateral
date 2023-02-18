
s="user"
# for i in s:
#     print(i)

#  iterable => they can't run next() method directly
#  iter()   , next()

stringIterator = iter(s)

print( next(stringIterator) )