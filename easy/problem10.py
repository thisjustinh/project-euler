# Find the sum of all the primes below two million.
def is_prime(n: int) -> bool:
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    return True

def prime_sum(limit: int) -> int:
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return sum(primes)

print(prime_sum(2000000))