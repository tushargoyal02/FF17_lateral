class Person:
    def __init__(self,id):
        self.id=id

    
   
    def test():
        print("Inside static method",Person.id)



p1=Person(10)
p1.test(p1,10,20)  #=> static right now
# p1.test(10,20)   # instance method 


print(p1.id)


def testFunc(data):
    print(data.id)

print("p1 here",p1)
testFunc(p1)