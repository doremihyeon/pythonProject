N =int(input())
num = list(map(int,input().split()))
big = list(set(big))
M = 0
for i in range(N):
    if num[i] > M:
        M = num[i]
        big.append(M)

print(big[-2])