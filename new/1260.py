import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph