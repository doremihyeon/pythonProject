# 입력 받기
N1_list = list(map(int, input()))  # 첫 번째 숫자를 배열로 받음
N2_list = list(map(int, input()))  # 두 번째 숫자를 배열로 받음

# 두 번째 숫자의 자릿수에 따라 곱셈 수행
a = int("".join(map(str, N1_list))) * N2_list[2]  # N2의 1의 자리
b = int("".join(map(str, N1_list))) * N2_list[1]  # N2의 10의 자리
c = int("".join(map(str, N1_list))) * N2_list[0]  # N2의 100의 자리

# 전체 곱셈 결과
result = int("".join(map(str, N1_list))) * int("".join(map(str, N2_list)))

# 결과 출력
print(a)
print(b)
print(c)
print(result)