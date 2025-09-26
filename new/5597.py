import sys
input = sys.stdin.readline

students = set(range(1, 31))   # 1~30까지 전체 학생
submitted = set(int(input().strip()) for _ in range(28))  # 제출한 28명

absence = sorted(list(students - submitted))  # 차집합 구하고 정렬

print(absence[0])
print(absence[1])

# import sys
# input = sys.stdin.readline

# n = [int(input().strip()) for _ in range(28)]  # 28명 입력 받기
# n.sort()  # 정렬

# absence = []  # 안 낸 학생 번호 담을 리스트

# num = 1  # 학생 번호 1부터 30까지 확인
# for i in range(28):
#     while num < n[i]:  # 제출한 번호보다 작은 번호가 있으면 빠진 것
#         absence.append(num)
#         num += 1
#     num = n[i] + 1  # 현재 번호는 제출했으니까 그 다음 번호로 이동

# # 마지막에 30까지 확인 (28명 입력 끝나고 남아 있을 수도 있음)
# while num <= 30:
#     absence.append(num)
#     num += 1

# print(absence[0])
# print(absence[1])