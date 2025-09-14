N = int(input())
arr = list(map(int,input().split()))
sum = 0

for i in range(N):
    sum += arr[i]

print(sum)