N = int(input())
res = 1 
cnt = 0

for i in range(1, N+1):
    res *= i

for c in str(res)[::-1]:
    if c != '0':
        break
    cnt += 1

print(cnt)