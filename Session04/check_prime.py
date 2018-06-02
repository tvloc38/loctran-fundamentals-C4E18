n = int(input("Enter a number: "))
is_prime = True

for i in range(2, n):
    if(n % i == 0):
        is_prime = False
        break

# output
if is_prime:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
            
    
