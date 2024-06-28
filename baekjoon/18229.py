N,M,K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
person = 0
count = 0
row_sum = [0] * N  # 각 행의 합을 저장할 리스트 초기화
flag = False
for i in range(M):
    for j in range(N):  # 각 사람에 대해 반복
        row_sum[j] += arr[j][i]  # 각 행의 합 누적
        if row_sum[j] >= K:  # 행의 합이 거리 기준 이상인 경우
            person = j + 1  # 결제한 사람의 번호 저장
            count = i + 1  # 결제한 횟수 저장
            flag = True
            break
    if flag:
        break
print(person, count)