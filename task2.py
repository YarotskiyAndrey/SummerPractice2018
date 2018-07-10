import random
import sys

n = sys.argv[1]

n = int(n)

print("%d random numbers:\n" % n)

for i in range(n):
    print("%.4f" % random.uniform(-1, 1))