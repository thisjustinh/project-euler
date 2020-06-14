# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    string = list(str(n))
    for i in range(len(string)):
        if not string[i] == string[-(i + 1)]:
            return False
    return True

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if j > i:
            continue
        product = i * j
        if is_palindrome(product) and product > max:
            max = product
print(max)
