N = int(input())
numbers = list(map(int, input().split()))
M = max(numbers)

for i in range(N):
    numbers[i] = numbers[i]/M*100

print(sum(numbers)/N)