class StudentDetail:
    student_id = 10
    student_name="tushar"
    student_email ="tushar@gmail.com"

    # method of my class
    def studentInfo(self):
        print("hello class studentDetail", self.student_email)
        return None


        

# we create an object of my class
student_obj1=StudentDetail()

print(student_obj1.student_id)

student_obj2=StudentDetail()
# print(student_obj1.student_name)

# print( student_obj1.studentInfo() )

# class variable changed with classname
StudentDetail.student_id=1010101


print( student_obj1.student_id)

print(StudentDetail.student_id)