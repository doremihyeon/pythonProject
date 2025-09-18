N = int(input())
num = list(map(int, input().split()))
cnt_len = 1
max_len = 1

for i in range(N):
    if num[i+1] - num[i] == 1:
            cnt += 1
            if cnt_len > max_len:
                  max_len = cnt_len
    else:
          cnt_len = 1

print(max_len)