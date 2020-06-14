# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def pythagorean_triplet() -> tuple:
    """
    Finds Pythagorean triplets using the Generalized Fibonacci Sequence
    """
    for h0 in range(1000):
        for h1 in range(1000):
            h2 = h0 + h1
            h3 = h1 + h2
            triple = [2*h1*h2, h0*h3, 2*h1*h2+h0**2]
            if sum(triple) == 1000:
                return triple, triple[0] * triple[1] * triple[2]

print(pythagorean_triplet())