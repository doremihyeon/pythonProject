N = int(input())
time = list(map(int,input().split()))
for i in range(len(time)):
    min = i
    for j in range(i+1,len(time)):
        if time[j] < time[min]:
            min = j #값이 아닌 위치를 저장
    time[i], time[min] = time[min], time[i]

sum = []
T = 0
for z in time:
    T += z
    sum.append(T)

All = 0
for x in sum:
    All += x

print(All)    