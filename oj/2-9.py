N = int(input())
measure = []
for i in range(1, N+1):
    if N % i == 0:
        measure.append(i)

print(*measure)