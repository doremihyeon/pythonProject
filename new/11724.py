import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]for _ in range(M+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
    
print(count)