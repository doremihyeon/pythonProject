A, B, V = map(int, input().split())
day = 0
height = 0

while True:
    day += 1
    height += A  # 올라가는 높이를 더해줌
    if height >= V:
        print(day)
        break
    height -= B  # 내려가는 높이를 빼줌