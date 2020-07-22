# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open('input/problem13.in') as fin:
    nums = list(map(int, fin.readlines()))

print(str(sum(nums))[0:10])