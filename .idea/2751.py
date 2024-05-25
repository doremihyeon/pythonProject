import sys # 시간초과로 인해 사용

N = int(input()) # 수의 개수 입력
num = [] #배열 생성
for _ in range(N): # 0-(N-1)까지 반복
    num.append(int(sys.stdin.readline())) # num배열에 정수 값들을 입력받아줌

num.sort() # num 배열을 정렬

for i in num: # num 배열의 각 요소를 반복
    print(i) # 현재 요소를 출력