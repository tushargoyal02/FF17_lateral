class Employee:
    _company="Futurense"
    __salary=19191

    def infoData():
        print(Employee.__salary)

class HRDepartment(Employee):
    department="HR"

#  name mangling => concept where the python the variable name if you put __ in the starting
e1=Employee()

#  __salary => _ClassName__salary

print(e1._company, Employee._Employee__salary)
Employee.infoData()

h1 = HRDepartment()
print(h1.department, h1._Employee__salary, "HR department")