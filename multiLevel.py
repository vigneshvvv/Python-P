class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class Address(Employee):
    def __init__(self, state, city, emp_id, name):
        Employee.__init__(self, emp_id, name)
        self.state = state
        self.city = city

class Developer(Address):
    def __init__(self, state, city, language, emp_id, name):
        super().__init__(state, city, emp_id, name)
        self.language = language

dev = Developer()
