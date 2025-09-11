import sys
input = sys.stdin.readline
N = int(input())
queue = []

for i in range(N):
    x = int(input())

    if x > 0:
        queue.append(x)

    else:
        print(max(queue))
        queue.pop(max(queue))
