graph = [[],
         [2, 3],
         [1, 3, 4],
         [1, 2],
         [2]]

visited = [False, False, False, False, False]

# define
def DFS(s):
    visited[s] = True
    for i in graph[s]:
        if visited[i] == False: #if not visited
            DFS(i)

DFS(1)