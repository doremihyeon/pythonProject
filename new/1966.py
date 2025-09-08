import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    case = map(int,input().split())
    queue = deque([(priority, idx)for idx, priority in enumerate(case)])
    order = 0

    while queue:
        current = queue.popleft()
        found = False

        for q in queue:
            if current[0] < q[0]:
                found = True
                break
        if found: #사실상 found == True라는 뜻
            queue.append(current)

        else:
            order += 1
            if current[1] == M:
                print(order)