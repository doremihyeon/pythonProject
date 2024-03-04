import sys
r = sys.stdin.readline().split()
N, M = map(int, r)
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k

for idx in range(1, N+1):
    print(basket[idx], end = ' ')