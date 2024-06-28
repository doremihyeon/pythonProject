import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    count = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            count += arr[a][b]

    print(count)