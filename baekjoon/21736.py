from collections import deque

N, M = list(map(int,input().split()))
matrix = []
for i in range(N+1):
    matrix.append(["X"])

for i in range(1, N+1):
    information = input()
    for character in information:
        matrix[i].append(character)

find = False
start_x, start_y = 0, 0
for r in range(1, N+1):
    for c in range(1, M+1):
        if matrix[r][c] == "I":
            start_x, start_y = r, c
            find = True
    if find:
        break

visited = []
for i in range(N+1):
    visited.append([])

for i in range(N+1):
    for j in range(M+1):
        visited[i].append(False)

def BFS(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    while q:
        X, Y = q.popleft()
        for i in range(4):
            xx = X + dx[i]
            yy = Y + dy[i]
            if (1 <= xx < N + 1) and (1 <= yy < M + 1):
                if not visited[xx][yy]:
                    if matrix[xx][yy] == "X":
                        continue
                    elif matrix[xx][yy] == "O":
                        visited[xx][yy] = True
                        q.append([xx, yy])
                    else: #matrix[xx][yy] == "P"
                        cnt += 1
                        q.append([xx, yy])
                        visited[xx][yy] = True

    return cnt

ans = BFS(start_x, start_y)
if ans == 0:
    print("TT")

else:
    print(ans)