N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if 0 < num :
        stack.append(num)

    else :
        if stack:
            stack.pop()

print(sum(stack))