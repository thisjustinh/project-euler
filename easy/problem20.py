# Find the sum of the digits in the number 100!

def factorial(n: int) -> int:
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

print(sum(map(int, list(str(factorial(100))))))