low = 0
high = 100

count = 0

print("Guess your number game")
input("Now think of a number from 0 to 100, then press Enter")
while True:
    mid = (low + high) // 2
    answer = input("Is {0} your number ".format(mid)).lower()
    if (answer == "s"):
        low = mid
    elif (answer == "l"):
        high = mid
    else:
        print("I knew it")
        break
    count += 1
    if count == 7:
        print("exit")
        break

