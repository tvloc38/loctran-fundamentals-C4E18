from getpass import getpass
username = "tvloc38"
password = "123456"
user = input("username:")
passwd = getpass("password:")

if user == username:
    if passwd != password:
        print("Wrong password")
    else:
        print("Welcome,", username)
else:
    print("No such user, go away")