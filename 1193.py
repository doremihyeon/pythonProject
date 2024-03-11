num = int(input())
line = 1 #현재 대각선의 위치(1번째에 위치)

while num > line: #몇 번째 대각선에 위치하는지 찾음
    num -= line
    line += 1 

# 짝수일경우
if line % 2 == 0: 
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')