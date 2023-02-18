#  constructor

#  object => constructor will be callee to initialize the memory locaiton

class Student:

    # dunder method
    def __init__(self,sid,sName,sEmail):
        self.sid=sid
        self.sName=sName
        self.sEmail=sEmail

    def studentInfo(self, salary):
        print("Student id :",self.sid*salary)

s1=Student(10,"Tushar","raj@gmail.com")

# print(s1.sid, s1.sName)
s1.studentInfo(99)