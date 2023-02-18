class AddingNumber:

    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2

    def __str__(self):
        return f"Adding number has {self.num1} {self.num2} "

    #  self => a1  , object=> a2
    def __add__(self, obj2):
        x = self.num1 + obj2.num1   # 20+40
        y=self.num2 + obj2.num2   #30+50
        return AddingNumber(x,y)



a1=AddingNumber(20,30)
a2=AddingNumber(40,50)

# print(a1)
# print(a2)

#  __add__(10,20)
# 10+20

print(a1 +a2)
#  a1.__add__(a2)
