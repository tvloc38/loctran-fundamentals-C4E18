# for i in range(3):
#     for i in range(5):
#         print("*", end='')
#     print()
# print("Hello", end=' ')
# print("World")
for i in range(10):
    for j in range(10):
        if (j <= 10 - i -1):
            print(" ", end='')
        else:
            print("*", end='')
   
    print()

