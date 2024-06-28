N = int(input())
cnt = 0
gom = set()  # gom이라는 집합을 생성

for _ in range(N):
    word = input()
    
    if word == 'ENTER':
        gom.clear()  # 'ENTER'이 들어오면 집합 gom의 내용을 비움
    else:
        if word not in gom:
            cnt += 1
            gom.add(word)  # set에 입력한 word값을 추가

print(cnt)