import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
queue = deque(range(1, N+1))
count = 0
result = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
        
print('<'+ ', '.join(map(str, result)) +'>')

