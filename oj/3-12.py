N = int(input())
num = list(map(int,input().split()))

unique_num = set(num)

print(*unique_num)