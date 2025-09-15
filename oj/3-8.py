import numpy

N = int(input())
num = list(map(int,input().split()))
avr = numpy.mean(num)
result = []

for i in range(N):
    if num[i] >= avr:
        result.append(num[i])

print(*result)