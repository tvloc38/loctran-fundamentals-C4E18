item = ["T-shirt", "Sweater"]

loop = True
while loop:
    x = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    if x == "R" or x == "r":
        print("Our items:", end=" ")
        print(*item, sep=", ")
    elif x == "C" or x == "c":
        c = input("Enter new item: ")
        item.append(c)
        print("Our items:", end=" ")
        print(*item, sep=", ")
    elif x == "U" or x == "u":
        while True:
            up_pos = int(input("Update position? "))
            if (up_pos > len(item) or up_pos < 1):
                print("Khong ton tai. Hay thu lai tu 1 den", len(item))
            else:
                break
        new_item =  input("New item? ")
        item[up_pos - 1] = new_item
        print("Our items:", end=" ")
        print(*item, sep=", ")
    elif x == "D" or x == "d":
        while True:
            del_pos = int(input("Delete position? "))
            if (del_pos > len(item) or del_pos < 1):
                print("Khong ton tai. Hay thu lai tu 1 den", len(item))
            else:
                break
        item.remove(item[del_pos - 1])
        print("Our items:", end=" ")
        print(*item, sep=", ")
    else:
        loop = False

