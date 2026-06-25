class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
class Address:
    def __init__(self, state, city):
        self.state = state
        self.city = city
    
class Developer(Employee, Address):
    def __init__(self, emp_id, name, state, city, language):
        Employee.__init__(self,emp_id, name)
        Address.__init__(self,state, city)
        self.language= language

    def printFun(self):
        print(self.state)
        print(self.emp_id)
        print(self.language)


dev = Developer(101, "Vignesh", "TN", "Chennai", "py")
dev.printFun()