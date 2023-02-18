class StudentMarks:

    def __init__(self,sName, sMarks):
        self.sName=sName
        self.sMarks=sMarks

    # self=s1
    def averageMarks(self):
        return sum(self.sMarks) / len(self.sMarks)

s1 = StudentMarks("Tushar",[33,44,55,66])

# print( s1.averageMarks() )



print("befre function",s1)
def average(studentobj):
    return sum(studentobj.sMarks) / len(studentobj.sMarks) 

print( average(s1))

