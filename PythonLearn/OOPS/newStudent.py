class Student:
    def __init__(self):
        self.marks=[]


    def __len__(self):
        return len(self.marks)

    @property
    def GraceMarks(self):
        print(self.marks[0] + 55 )

s1=Student()
s1.marks.append(74)
s1.marks.append(201)
print(s1.marks)

# print(len(s1))
#  s1.__len__(self=s1)


s1.GraceMarks