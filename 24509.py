import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

res = []
for c in range(4):
    maximum = -1
    student = -1
    for r in range(N):
        if arr[r][0] not in res:
            if arr[r][c + 1] > maximum:
                maximum = arr[r][c + 1]
                student = arr[r][0]
    res.append(student)

print(*res)