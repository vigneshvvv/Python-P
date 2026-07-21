userName = "Vignesh"
passwordN = "Vignesh"
attempts = 1
login = False

while attempts < 4:
    user = input("Enter your userName: ")
    password = input("Enter your password: ")

    if user == userName and password == passwordN:
        print("Login successful")
        login = True
        break
    else:
        print(f"Either userName or password incorrect.Attempts remaning {3-attempts}")
        attempts += 1

if login == False:
    print("Maximum attempt reached.")
