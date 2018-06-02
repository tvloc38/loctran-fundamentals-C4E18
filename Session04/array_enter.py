n = input("Enter a sequence of number: ")
words = n.strip().split(" ") # strip: bo cac ki tu la (dau cach, tab, ..)

numbers = []

for item in words:
    numbers.append(int(item))

is_sorted = True

for i in range(0,len(numbers)-1):
    if (numbers[i] > numbers[i+1]):
        is_sorted = False
        break

if is_sorted:
    print(numbers)
else:
    new_numbers = []
    while True:
        new_numbers.append(min(numbers))
        numbers.remove(min(numbers))

        if len(numbers) == 0:
            break
    print(new_numbers)

    #s.replace ???
