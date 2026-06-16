users = [{
    "userName": "vignesh",
    "password": "vignesh@123"
},
{
    "userName": "kumar",
    "password": "kumar@123"
},
{
    "userName": "deva",
    "password": "deva"

}]

userName = input("Enter your UserName: ")
password = input("Enter your password: ")

# login_success = False

for user in users:
    if user["userName"] == userName and user["password"] == password:
        # login_success = True
        print("login successful")
        break
    else:
        print("Either username or password is incorrect")

# if login_success:
#     print("login successful")
# else:
#     print("Either username or password is incorrect")
