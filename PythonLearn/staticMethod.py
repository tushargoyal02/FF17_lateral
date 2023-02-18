
class Student:
    schoolName="Miles Education"
    salary=7000
    #  self.age=age
    #  self = "hey"

    def __init__(self,x):
        self.newhike=x

    @staticmethod
    def schoolInfo():
        Student.schoolName="tushar"
        

print(Student.schoolName)

Student.schoolInfo()

print(Student.schoolName)