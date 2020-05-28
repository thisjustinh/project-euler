# Find the sum of all multiples of 3 and 5 below 1000
print(sum([i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(1000)]))
