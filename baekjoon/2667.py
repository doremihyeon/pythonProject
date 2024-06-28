from collections import deque

N = int(input())
matrix = []
for i in range(N):
    matrix.append([])

for i in range(N):
    information = input()
    for j in range(N):
        matrix[i].append(information[j])
arr = []

visited = []
for i in range(N):
    visited.append([])

for i in range(N):
    for j in range(N):
        visited[i].append(False)

def BFS(sr, sc):
    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1

    while q:
        X, Y = q.popleft()
        for i in range(4):
            xx = X + dx[i]
            yy = Y + dy[i]
            if (0 <= xx < N) and (0 <= yy < N):
                if not visited[xx][yy]:
                    if matrix[xx][yy] == "1":
                        cnt += 1
                        visited[xx][yy] = True
                        q.append([xx, yy])
                    elif matrix[xx][yy] == "0":
                        continue

    arr.append(cnt)

count = 0

for r in range(N):
    for c in range(N):
        if not visited[r][c] and matrix[r][c] == "1":
            BFS(r, c)
            count += 1

print(count)
arr.sort()
for num in arr:
    print(num)