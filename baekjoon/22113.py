N, M = map(int, input().split())

bus_num = list(map(int,input().split()))

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

cost = 0
for i in range(M-1):
    cost += board[bus_num[i]-1][bus_num[i+1]-1]

print(cost)