class Employee:
    def __init__(self):
        print("EmployeeClass")
        
    def hello(self):
        print("hello employee")

class Driver(Employee):
    def __init__(self):
        super().__init__()
        
    def hello(self):
        print("hello Driver")

class Customer(Driver):
    def __init__(self):
        super().__init__()

    def hello(self):
        print("hello customer")
        


c1=Customer()
c1.hello()


