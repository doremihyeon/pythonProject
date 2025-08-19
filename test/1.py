N = int(input())
price = list(map(int, input().split()))

min_num = price[0]
max_num = 0

for i in price:
    if i < min_num:
        min_num = i

    P = i - min_num

    if P > max_num:
        max_num = P


print(max_num)    