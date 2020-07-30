# Evaluate the sum of all the amicable numbers under 10000.

def d(n: int) -> int:
    """
    Sum of the proper divisors of n
    """
    divisors = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            divisors.append(i)
            if not i == 1 and not i ** 2 == n:
                divisors.append(n // i)
    return sum(divisors)

def are_amicable(a: int, b: int):
    if d(a) == b and d(b) == a:
        return True
    return False

amicables = []
for i in range(1, 10000):
    for j in range(1, 10000):
        if i > j:
            continue
        elif are_amicable(i, j):
            if not i in amicables:
                amicables.append(i)
            if not j in amicables:
                amicables.append(j)
        print(i, j)
print(sum(amicables))
