N = int(input())
arr= []

for _ in range(N):
    arr.append(input().strip())
set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)