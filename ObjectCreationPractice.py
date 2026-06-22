class userRegistration:
    userId = 0
    firstName = ""
    lastName = ""

    def __init__(self, userId, firstName, lastName):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
    

# user1 = userRegistration()
# user1.userId = 121
# user1.firstName = "vignesh"
# user1.lastName = "kumar"

# user2= userRegistration()
# user2.userId = 134
# user2.firstName = "Deva"
# user2.lastName = "Narashiman"

# print(user1.userId)

user1 = userRegistration(121, "deva", "Narashiman")

print(user1)

