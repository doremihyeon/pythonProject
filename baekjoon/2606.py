from collections import deque
def BFS(s):
    queue = deque()

    visited[s] = True
    queue.append(s)

    while queue:
        nxt = queue.popleft()
        for i in graph[nxt]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N = int(input())
graph = []
visited = [False] * (N+1)
for i in range(N+1):
    graph.append([])

E = int(input())
for i in range(E):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)


BFS(1)
answer = 0
for i in range(1, N+1):
    if visited[i]:
        answer += 1
print(answer-1)