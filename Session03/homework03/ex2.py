sheep = [5, 7, 300, 90, 24, 50, 75]

# 2.1
print("Hello, my name is Loc and these are my sheep sizes")
print(sheep)

loop = True
count = 1;

while loop:
    print("Month", count) 

    # 2.4
    for i in range(len(sheep)):
        sheep[i] += 50
    print("One month has passed, now here is my flock")
    print(sheep)

    # 2.2
    print ("Now my biggest sheep has size", max(sheep), "let's shear it")

    # 2.3
    num_max = sheep.index(max(sheep))
    sheep[num_max] = 8
    print("After shearing, here is my flock")
    print(sheep)

    print("*" * 10)

    count += 1
    if count == 4:
        loop = False
        for i in range(len(sheep)):
            sheep[i] += 50
        print("One month has passed, now here is my flock")
        print(sheep)

sum = 0
for i in range(len(sheep)):
    sum += sheep[i]
print("My flock has size in total: ", sum)
print("I would get ", sum, " * 2$ = ", sum*2,"$", sep="")