size = int(input("Nhap co chu: "))
mid = size//2
for i in range(size):
    for j in range(size*4+3):
        if i == 0 or i == (size-1):
            if j == size or j == (2*size+1) or j == (3*size+1) or j == (3*size+2):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i == mid:
            if j == 0 or j == (size+1) or j == (2*size) or j == (2*size+2) or j == (3*size+1) or j > (3*size+2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j == 0 or j == (size+1) or j == (2*size) or j == (2*size+2) or j == (3*size+1) or j == (3*size+3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()