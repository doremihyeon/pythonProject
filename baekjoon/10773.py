K = int(input())
stack = []
ts = 0

for i in range(K):
    num = int(input())

    if num == 0:
        ts -= stack.pop()

    else:
        stack.append(num)
        ts += num

print(ts)