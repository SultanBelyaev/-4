n = int(input())
D = [0] * n
from random import randint
for i in range(n):
    D[i] = randint(-5, 510)
m = D.index(max(D)) + 1
for i in range(n - m):
    D[m + i] = 0
print(D)
