K = int(input())
stack = []
total_sum = 0

for i in range(K):
    num = int(input())

    if num == 0:
        total_sum -= stack.pop()

    else:
        stack.append(num)
        total_sum += num

print(total_sum)