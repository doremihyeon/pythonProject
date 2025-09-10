import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
location = list(map(int,input().split()))
queue = deque(range(1, N+1))
result = 0

for target in location:
    idx = queue.index(target)
    
    left = idx
    right = len(queue) - idx

    if left <= right :
        queue.rotate(-left)
        queue.popleft()
        result += left
    else :
        queue.rotate(right)
        queue.popleft()
        result += right

print(result)