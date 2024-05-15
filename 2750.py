N = int(input())  # 사용자로부터 정수 N을 입력받음
list_num = []  # 숫자들을 저장할 빈 리스트 생성

for _ in range(N):
    num = int(input())  # 정수를 입력받고
    list_num.append(num)  # 리스트에 추가

list_num.sort()  # 리스트를 정렬

for num in list_num:  # 정렬된 리스트의 각 요소를 출력
    print(num)
