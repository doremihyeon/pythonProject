N = int(input())
num = list(map(int,input().split()))
M = 0
P = 0
for i in num:
    if i < 0:
        M += 1

    elif i > 0:
        P += 1

print(P)
print(M)