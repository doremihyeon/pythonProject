from collections import deque
import sys
input = sys.stdin.readline


T = int(input())


def BFS(sr, sc):  #start r, start c
    q = deque()
    q.append([sr, sc])
    matrix[sr][sc] = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    while q:
        # coordinate = q.popleft()
        # nxt_r = coordinate[0]
        # nxt_c = coordinate[1]
        nxt_r, nxt_c = q.popleft()
        for i in range(4):
            rr = nxt_r + dr[i]
            cc = nxt_c + dc[i]
            if 0 <= rr < R and 0 <= cc < C:
                if matrix[rr][cc] == 1:
                    matrix[rr][cc] = 0
                    q.append([rr, cc])


for _ in range(T):
    # 가로, 세로, 배추의 개수
    C, R, K = list(map(int, input().split()))
    matrix = []
    for i in range(R):
        matrix.append([])

    for i in range(R):
        arr = matrix[i]
        for j in range(C):
            arr.append(0)

    # print(matrix)

    for i in range(K):
        y, x = list(map(int, input().split()))
        matrix[x][y] = 1

    # print(matrix)

    ans = 0
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 1:
                BFS(r, c)
                ans += 1
    print(ans)