class Employee:
    def __init__(self,name, email, wallet):
        self.name=name
        self.email=email
        self.wallet=wallet

    def info(self):
        print("Employee class")


class Driver(Employee):
    def __init__(self,name, email, wallet):
        self.name=name
        self.email=email
        self.wallet=wallet

    def dinfo(self):
        print("Driver class")


d1= Driver("raj","raj@gmail.com",2201)

#  inheritence ( set the relation )
class Customer(Driver):
    def __init__(self,name, email, wallet, trip_status):
        
        super().__init__(name,email,wallet)

        self.trip_status=trip_status

        # Employee.info(self)

c1=Customer("Naina","nainatalwar@gmail.com",300,"Active")

c1.dinfo()
c1.info()


