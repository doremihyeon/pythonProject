import sys
input = sys.stdin.readline

N, M = map(int,input().split())
chess = []
result = float('inf') #초기값 무한대로 설정

for _ in range(N):
    line = input().strip()
    chess.append(list(line))

for row in range(N-7): #행 시작
    for col in range(M-7): #열 시작
        repaint_w = 0
        repaint_b = 0

        for x in range(row, row+8):
            for y in range(col, col+8):
                    
                if (x+y) % 2 == 0: #짝수 칸
                    if chess[x][y] != 'B':
                        repaint_b += 1

                    if chess[x][y] != 'W':
                        repaint_w += 1

                else:
                    if chess[x][y] != 'B':
                        repaint_w += 1

                    if chess[x][y] != 'W':
                        repaint_b += 1
       
        result = min(result, repaint_w, repaint_b)

print(result)