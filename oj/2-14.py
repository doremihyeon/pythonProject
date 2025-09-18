N = int(input())
num = list(map(int,input().split()))
result = 0

for i in num:
    if 10 <= i <= 50:
        result += 1

print(result)