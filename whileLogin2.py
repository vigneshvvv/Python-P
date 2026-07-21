userName = "Vignesh"
passwordN = "Vignesh"
attempts = 1


while attempts > 0:
    if attempts == 4:
        print("Maximum attempts reached")
        break
    userN = input("Enter your userName")
    password = input("Enter your password: ")

    if userN == userName and passwordN == password:
        print("login Successful.")
        break
    else:
        print(f"Either userName or password incorrect.Attempts remaning {3-attempts}")
        attempts += 1
        