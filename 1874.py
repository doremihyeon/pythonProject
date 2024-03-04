n = int(input())
stack = []
start = 1
sign = []

for _ in range(n):
    end = int(input())
    while start <= end:
        stack.append(start)
        sign.append('+')
        start += 1

    if stack[-1] == end:
        stack.pop()
        sign.append('-')

    else:
        print("NO")
        break

else:
    for i in sign:
        print(i)