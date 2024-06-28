N = int(input())
cnt = 0
num = 1
while True:
    if "666" in str(num):
        cnt = cnt+1

    if cnt == N:
        print(num)
        break

    num=num+1