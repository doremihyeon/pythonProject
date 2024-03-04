N = int(input())
C = []

for _ in range(N):
    x, y = map(int, input().split())
    C.append((x, y))
C.sort()
for i in range(N):
    print(C[i][0], C[i][1])