edges = []
parent = [i for i in range(7)] 

for i in range(6):
    a, b = map(int,input().split())
    edges.append((a, b))

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

for a, b in edges:
    if find(a) != find(b):
        union(a, b)
        
print(*parent)