N = int(input())
A = list(map(int,input().split()))
find = int(input())
count = 0

for i in range(N):
    if A[i] == find:
        count += 1

print(count)