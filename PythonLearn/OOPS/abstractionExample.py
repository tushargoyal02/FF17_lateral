from abc import ABC, abstractmethod

#  abc => package, ABC => class ( abstract base class)
#  company class is now abstract class => blue print for all the child classes
class Company(ABC):
    company_name="Futurense"

    @abstractmethod
    def department(self):
        pass

    #normal method
    def ownerInfo(self):
        print("hey the owner is Raghav")

class Marketing_dept(Company):
    
    def department(self):
        print("hey we belong to Marketing department")


class HR_dept(Company):
    def department(self):
        print("hey this is my hr department class")

h1= HR_dept()
h1.department()
h1.ownerInfo()
# c1=Company()
# print(c1.company_name)