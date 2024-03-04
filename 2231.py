N = int(input())
M = 0

for i in range(1, N+1):
    num = sum((map(int, str(i))))
    M = i + num

    if M == N:
        print(i)
        break
if i == N:
    print(0)