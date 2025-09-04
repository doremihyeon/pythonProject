import sys
input = sys.stdin.readline

N = int(input())
queue = []
result = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        queue.append(int(cmd[1]))

    if cmd[0] == "pop":
        if queue:
            result.append(queue.pop(0))

        else:
            result.append(-1)

    if cmd[0] == "size":
        result.append(len(queue))

    if cmd[0] == "empty":
        if queue:
            result.append(0)
        
        else:
            result.append(1)

    if cmd[0] == "front":
        if queue:
            result.append(queue[0])
        
        else:
            result.append(-1)
    
    if cmd[0] == "back":
        if queue:
            result.append(queue[-1])
        
        else:
            result.append(-1)

print(*result, sep="\n")

# deque 방법으로 푸는법
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# queue = deque()
# result = []

# for _ in range(N):
#     cmd = input().split()

#     if cmd[0] == "push":
#         queue.append(int(cmd[1]))
#     elif cmd[0] == "pop":
#         result.append(queue.popleft() if queue else -1)
#     elif cmd[0] == "size":
#         result.append(len(queue))
#     elif cmd[0] == "empty":
#         result.append(0 if queue else 1)
#     elif cmd[0] == "front":
#         result.append(queue[0] if queue else -1)
#     elif cmd[0] == "back":
#         result.append(queue[-1] if queue else -1)

# print("\n".join(map(str, result)))