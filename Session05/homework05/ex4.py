# Fibonacci sequence
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)
    

rabbit = 1
for i in range(5):
    rabbit += F(i)
    print("Month {0} : {1} pair(s) of rabbit".format(i, rabbit))