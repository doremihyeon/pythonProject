N = int(input())
big = []

for _ in range(N):
    x, y = map(int, input().split())
    big.append((x, y))

for i in big:
    R = 1
    for j in big:
        if i[0] < j[0] and i[1] < j[1]:
            R += 1
    print(R, end=" ")