n = int(input("How many B bacterias are there? "))
t = int(input("How much time in minute will we wait? "))
bac = n * (2 ** (t // 2))
print("After {0} mins, we would have {1} bacterias".format(t,bac))