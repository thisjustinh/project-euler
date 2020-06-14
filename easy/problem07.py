# What is the 10 001st prime number?

def is_prime(n: int) -> bool:
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

primes = []

i = 2
while len(primes) <= 10000:  # last added term will be the 10001st prime
    if is_prime(i):
        primes.append(i)
    i += 1
print(primes)
print(len(primes))