yob = int(input("Nam sinh cua ban la:"))

age = 2018 - yob

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
elif age == 24:
    print("24")
else:
    print("Adult")

print("Bye")