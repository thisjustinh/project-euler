# Which starting number, under one million, produces the longest Collatz chain?

max_length = 0
start = 0
for i in range(1, 1000000):
    # generate collatz seq
    collatz = [i]
    n = collatz[-1]
    while n != 1:
        if n % 2:
            collatz.append(3 * n + 1)
        else:
            collatz.append(n / 2)
        n = collatz[-1]
    if len(collatz) > max_length:
        max_length = len(collatz)
        start = i
    print(i)
print(start)
