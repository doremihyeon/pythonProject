N = int(input())
num = list(map(int, input().split()))  # 숫자로 저장
result = 0

for i in range(N):
    if num[i] % 2 == 0:   # 바로 정수로 체크 가능
        result += num[i]  # 정수끼리 합산

print(result)