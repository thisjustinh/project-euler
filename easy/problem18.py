def print_t(t: list):
    result = [str(line) for line in t]
    print('\n'.join(result))

with open('input/problem18.in') as f:
    triangle = f.readlines()
    triangle = [list(map(int, line.strip().split())) for line in triangle]

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    print_t(triangle)