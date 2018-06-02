from getpass import getpass
user = input("Username: ")
count = 0
while user == "c4e":
    passwd = getpass("Password: ")
    if (passwd == "codethechange"):
        print("Welcome, c4e")
        break
    else:
        print("Password is incorrect")
        count += 1
        if count == 3:
            print("You failed to log in 3 times, go away")
            break
print("Try again")
    

