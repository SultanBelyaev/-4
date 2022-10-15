n = int(input())
A = [0] * n
delta = int(input())
from random import randint
for i in range(n):
    A[i] = randint(-5, 510)
print(n - delta)
