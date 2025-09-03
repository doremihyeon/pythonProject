import sys
input = sys.stdin.readline

N = int(input())
result = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        result.append(int(cmd[1]))

    if cmd[0] == "pop":
        if result:
            print(result.pop())
        
        else:
            print('-1')

    if cmd[0] == "size":
        print(len(result))
   
    if cmd[0] == "empty":
        print(0 if result else 1)
    
    if cmd[0] == "top":
        print(result[-1] if result else -1)