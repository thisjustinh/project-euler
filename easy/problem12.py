# What is the value of the first triangle number to have over five hundred divisors?

def count_divisors(n: int):
    count = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            if i ** 2 == n:
                count += 1
            else:
                count += 2
    return count

n_divisors = 0
n_terms = 2
while n_divisors < 500:
    n = sum([i for i in range(1, n_terms)])
    n_divisors = count_divisors(n)
    n_terms += 1

print(n)