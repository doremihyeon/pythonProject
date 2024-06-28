N = int(input())
arr = []
answer = 0

for _ in range(N):
    word = input()
    arr.append(word)

for i in arr:
    dic = {}
    last = i[0]
    isbreak = False
    for j in i:
        if last != j and dic.get(j, -1) != -1:
            isbreak = True
            break
        dic[j] = dic.get(j, 0) + 1
        last = j
    if not isbreak:
        answer += 1

print(answer)