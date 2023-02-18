class GenerateNumber:
    def __init__(self):
        print("hey")
        self.count=0
    
    def __next__(self):
        if self.count<10:
            current=self.count
            self.count +=1
            return current

        else:
            raise StopIterationError

class iterableGenerate:
    def __iter__(self):
        return GenerateNumber()



for i in iterableGenerate():
    print(i)
    
# print(iterableGenerate() )

g1=GenerateNumber()
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
