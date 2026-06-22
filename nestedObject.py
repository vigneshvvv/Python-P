class Employee: 
    name = ""
    address = {}

    class Address:

        city = ""
        state = ""

        def __init__(self, city, state):
            self.city = city
            self.state = state

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("city:", self.address.city)
        print("state:", self.address.state)


add = Employee.Address("Chennai", "TamilNadu")
emp = Employee("vignesh", add)

emp.display()