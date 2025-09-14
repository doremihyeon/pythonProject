N = int(input())
arr = list(map(int,input().split()))
result = []

for i in range(N):
    if arr[i] % 2 == 0:
        result.append(arr[i])

print(*result)