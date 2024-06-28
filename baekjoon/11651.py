N = int(input())
C = []

for _ in range(N):
    x, y = map(int, input().split())
    C.append((x, y))

C.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(C[i][0], C[i][1])