N, k = map(int,input().split()) # N(사람 수), k(수상인원) 공백을 포함하여 입력을 받아줌
scr = map(int,input().split()) # 점수를 입력받음
print(sorted(scr)[-k]) # 점수를 정렬하고 k번째 사람의 값을 출력함