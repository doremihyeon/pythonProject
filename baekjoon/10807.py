import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
count = 0

for i in range(N):
    if num[i] == v:
        count += 1
print(count)