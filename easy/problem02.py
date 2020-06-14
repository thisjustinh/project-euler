# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def even_fib_seq(limit: int) -> list:
    seq = []
    n1 = 1
    n2 = 1
    while n1 + n2 <= limit:
        fib = n1 + n2
        if fib % 2 == 0:
            seq.append(fib)
        n1 = n2
        n2 = fib
    return seq

print(sum(even_fib_seq(4000000)))