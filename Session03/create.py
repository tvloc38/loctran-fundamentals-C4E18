fav = ["an", "ngu", "lam viec"]

print("Hi there, here you favorite things so far", end=" ")
print(*fav, sep=", ")

add = input("Name one thing you want to add? ")
fav.append(add)

print("Hi there, here you favorite things so far", end=" ")
print(*fav, sep=", ")