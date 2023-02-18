class AddNumber:
    def addition1(self,x,y):
        return x+y




class SubNumber:
    def subtract1(self,x,y):
        return x-y





class ArithmeticOPeration(AddNumber,SubNumber):
    def mulitply(self,x,y):
        return x*y


a1=ArithmeticOPeration()

print( a1.mulitply(10,20) )

print( a1.addition1(10,20) )