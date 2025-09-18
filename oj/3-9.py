N = int(input())
num = list(map(int,input().split()))
M = 0
index = 0
for i in range(N):
    if num[i] > M:
        M = num[i]
        index = i
print(index)