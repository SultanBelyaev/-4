from random import randint
n = int(input())
m = int(input())
A = [0] * n
B = [0] * m
for i in range(n):
    A[i] = randint(-5, 510)
for i in range(m):
    B[i] = randint(-5, 510)
for i in A:
    for g in B:
        if i == g:
            print(i,end =" ")