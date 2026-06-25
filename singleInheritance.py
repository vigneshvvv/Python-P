# parant class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")

class Developer(Employee):
    def __init__(self, emp_id, name, language):
        super().__init__(emp_id, name)
        self.language = language
    
    def work(self):
        print(f"{self.name} developing using {self.language}")

class Manager(Employee):
    def __init__(self, emp_id, name, teamSize):
        super().__init__(emp_id, name)
        self.teamSize = teamSize
    def work(self):
        print(f"{self.name} managing {self.teamSize} members")

dev = Developer(101, "vignesh", "PY")
dev.work()

manager = Manager(102, "deva", 10)
manager.work()



