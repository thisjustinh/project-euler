# What is the largest prime factor of the number 600851475143?
def is_prime(n: int) -> bool:
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    return True

def prime_factorization(n: int) -> list:
    factors = []
    for i in range(2, int(n ** (1/2))):
        if is_prime(i) and n % i == 0:
            factors.append(i)
    return factors

print(prime_factorization(600851475143))