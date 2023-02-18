class Student:
    age=10



s1=Student()

print(s1.age)

print(Student.age)

print("After change in the class object")

s1.age=99
print(s1.age,"AFter change")
Student.age=88
print(Student.age, s1.age,"AFter change")

s2=Student()
print(s2.age)