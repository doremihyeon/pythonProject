import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 정점 번호가 작은 것부터 방문하기 위해 정렬
for i in range(1, N+1):
    graph[i].sort()

# DFS
DFS_result = []
visited_dfs = [False] * (N+1)

def dfs(v):
    visited_dfs[v] = True
    DFS_result.append(v)
    for nxt in graph[v]:
        if not visited_dfs[nxt]:
            dfs(nxt)

dfs(V)

# BFS
BFS_result = []
visited_bfs = [False] * (N+1)
queue = deque([V])
visited_bfs[V] = True

while queue:
    v = queue.popleft()
    BFS_result.append(v)
    for nxt in graph[v]:
        if not visited_bfs[nxt]:
            queue.append(nxt)
            visited_bfs[nxt] = True

# 출력
print(*DFS_result)
print(*BFS_result)