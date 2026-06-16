class userDetail:
    id = 0
    firstName= ""
    lastName = ""
    salary = 0
    age = 0
    __role = ""
    _experience = 0

    def __init__(self):
        pass

    def __init__(self, id, firstName, lastName, salary, age):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.age = age
    
    def print(self):
        print("function working")

    def getRole(self):
        return self.__role

    def setRole(self, role):
        self.__role = role

    def getExp(self, exp):
        self._experience = exp

    def getExp(self):
        return self._experience

user = userDetail(1, "vignesh", "kumar", 40000, 25)
user.setRole("Tester")
user._experience = 10
print(user.getRole())

user.print()
print(user.firstName)


