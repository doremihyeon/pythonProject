N = int(input())
num = list(map(int, input().split()))
Prime_num = 0

for x in num:
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                Prime_num += 1
            break
print(Prime_num)
# 3,9