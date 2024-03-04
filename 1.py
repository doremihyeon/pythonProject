from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]

def BFS(sr, sc):
    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = True
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt = -1  # Start with -1 since we increment before appending the first element

    while q:
        X, Y = q.popleft()
        for i in range(4):  # Fixed the loop variable here
            xx = X + dx[i]
            yy = Y + dy[i]
            if (0 <= xx < N) and (0 <= yy < M):
                if not visited[xx][yy] and matrix[xx][yy] == 0:
                    cnt += 1
                    visited[xx][yy] = True
                    q.append([xx, yy])

    return cnt

total_days = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            days = BFS(i, j)
            if days == -1:  # If any tomato remains unreachable
                print(-1)
                sys.exit()
            total_days = max(total_days, days)

print(total_days)