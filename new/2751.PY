import sys
input = sys.stdin.readline 

N = int(input())
num_sort = []
for i in range(N):
    num = int(input())
    num_sort.append(num)
num_sort.sort()

for i in range(N):
    print(num_sort[i])