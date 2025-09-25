import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]
DFS = []
BFS = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def dfs(v):
    visted = [False] * (N+1)
    visted[v] = True
    DFS.append(v)

    for next in graph[v]:
        if not visted[next]:
            dfs(next)

def bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    BFS.append(start)

    while queue:
        v = queue.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True
                BFS.append(nxt)