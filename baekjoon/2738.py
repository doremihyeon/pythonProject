N, M = map(int, input().split())
A, B = [], []
for r in range(N):
    A.append(list(map(int, input().split())))

for r in range(N):
    B.append(list(map(int, input().split())))

for r in range(N):
    for c in range(M):
        print(A[r][c] + B[r][c], end=' ')
    print()