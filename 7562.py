from collections import deque
def BFS(sr, sc):
    q = deque()
    q.append([sr, sc, 0])
    matrix[sr][sc] = True
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, 2, 2, -2, -2]

    while q:
        X, Y, t = q.popleft()
        if X == X2 and Y == Y2:
            return t
        for i in range(8):
            xx = X + dx[i]
            yy = Y + dy[i]
            if (0 <= xx < N) and (0 <= yy < N):
                if matrix[xx][yy] == False:
                    q.append([xx, yy, t+1])
                    matrix[xx][yy] = True

T = int(input())
for _ in range(T):
    N = int(input())
    X1, Y1 = map(int, input().split())
    X2, Y2 = map(int, input().split())

    matrix = []
    for i in range(N):
        matrix.append([])

    for i in range(N):
        for j in range(N):
            matrix[i].append(False)

    answer = BFS(X1, Y1)
    print(answer)