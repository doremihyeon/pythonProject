import sys
input = sys.stdin.readline

students = set(range(1, 31))   # 1~30까지 전체 학생
submitted = set(int(input().strip()) for _ in range(28))  # 제출한 28명

absence = sorted(list(students - submitted))  # 차집합 구하고 정렬

print(absence[0])
print(absence[1])