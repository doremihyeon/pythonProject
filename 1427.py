N = int(input()) # 입력 값을 받아줌
sum = [] # 배열을 만듬

for i in str(N): # 정수를 문자열로 변환하여 각 자릿수를 개별로 접근
    sum.append(int(i)) # 정수로 변활하여 배열에 값에 넣어줌
sum.sort(reverse = True) # 내림차순으로 정렬하는 함수 사용

for i in sum: # sum의 각 요소를 순회하며 출력
    print(i, end = '') # 옵션을 사용하여 각 숫자를 공백 없이 출력