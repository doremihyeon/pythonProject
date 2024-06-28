cnt = int(input())
S = []
paper = [[0] * 100 for _ in range(100)]
count = 0

for _ in range(cnt):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                count += 1

print(count)
 