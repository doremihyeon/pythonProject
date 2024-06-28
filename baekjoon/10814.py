N = int(input())

arr = []
for i in range(N):
    Y, name = input().split()
    arr.append([int(Y), name])

arr.sort(key=lambda x: x[0])
for i in arr:
    print(i[0], i[1])