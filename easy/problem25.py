i = 2
n1 = 1
n2 = 1
while len(str(n2)) < 1000:
    fib = n1 + n2
    n1, n2 = n2, fib
    i += 1
print(i)