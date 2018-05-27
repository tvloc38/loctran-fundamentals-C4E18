# list (array)
# create
menu = [
    "food1", "food2", "food3", "food4"
]

# seperator
# read
# print(*menu, sep=", ")
# print(len(menu)) #dem so luong

# menu.append("food5") #add

# print(*menu, sep=", ")
# print(len(menu))

first_item = menu[1] # 0:first  -1:last
# print(first_item)

# for i in range(len(menu)):
#     # print(i + 1, menu[i], sep=". ")
#     print("{0}. {1}".format(i + 1, menu[i])) #string formatting

for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))

# for item in menu:
#     print(item)

# update
# menu[2] = "Cua"
# print(*menu, sep=", ")

n = int(input("Position you want to update: "))
add = input("Your replacing favorite: ")

menu[n-1]= add

for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))
#CRUD = Create - Read - Update - Delete 