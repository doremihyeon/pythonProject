N = int(input())
A = list(map(int,input().split()))
B = []

for i in range(1, N):
    B.append(A[i])

B.append(A[0])

print(*B)
