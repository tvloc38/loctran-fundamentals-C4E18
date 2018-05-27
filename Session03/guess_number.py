from random import randint

x = randint(1,100)


count = 0
loop = True

while loop:
    y = int(input("Guess my number (1-100): "))
    count += 1
    if count == 7:
        print(count, "You lose")
        loop = False
    else:
        if y < x:
            if (x - y) < 10:
                print(count, "A little too small")
            else:
                print(count, "too small")
        elif y > x:
            if (y - x) < 10:
                print(count, "A little too large")
            else:
                print(count, "too large")
        elif y == x:
            print(count, "Bingo")
            loop = False
    

