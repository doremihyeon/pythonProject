n = int(input())
for _ in range(n):
    a = input()
    score = 0
    sum_score = 0
    for i in a:
        if i == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)