import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
edges = []
parent = [i for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

total = 0
max_cost = []
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        total += c
        max_cost.append(c)

print(total- max(max_cost))