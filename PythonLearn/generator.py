

def func():
    count=0

    while count<100:
        yield count  # you program has paused
        
        count+=1
        

g=func()

print( next(g) )
print( g.__next__())


# # x=func()

# for data in func():
#     print(data)


