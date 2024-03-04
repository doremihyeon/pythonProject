# 입력받기
S = input()
# 배열초기화
arr = []
for i in range(len(S)):
    # 현재 문자의 알파벳 위치 계산
    index = ord(S[i]) - ord('a')

    # 해당 알파벳의 위치가 아직 초기화되지 않았으면 저장
    if arr[index] == -1:
        arr[index] = i

# 결과 출력
for element in arr:
    print(element, end=' ')
