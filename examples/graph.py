import random
import matplotlib.pyplot as plt

def geometric_distribution(n: int) -> list:
  counts = []
  for i in range(n):
    heads = False
    flips = 0
    while not heads:
      flips += 1
      result = random.randrange(0, 2)
      if result == 0:
        heads = True
    counts.append(flips)
  return counts

flips = geometric_distribution(1000)
plt.hist(flips)
plt.show()