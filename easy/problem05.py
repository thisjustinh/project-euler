# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 2520
found = False

while not found:
    divisible = True
    for j in range(11,21):
        if not i % j == 0:
            divisible = False
        if not divisible:
            print(i, "failed")
            break
    if divisible:
        print(i)
        found = True
    i += 2520