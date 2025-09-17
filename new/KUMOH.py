import sys
input = sys.stdin.readline

N = int(input())
S = []
M = 0
starts = []
answer = 0

# 문자열 입력
for _ in range(N):
    S.append(input().strip())

# 최대 열 길이
for row in S:
    if len(row) > M:
        M = len(row)

# 대각선 시작점들
for i in range(N):
    starts.append((i, 0))
for j in range(1, M):
    starts.append((N-1, j))

for (r, c) in starts:
    t = ""
    i, j = r, c
    while i >= 0 and j < M:
        t += S[i][j]
        i -= 1
        j += 1
    
    x = t.count("KUMOH")
    y = t[::-1].count("KUMOH")
    answer += max(x, y)

print(answer)