T = int(input())

for i in range(T):
    C, W = input().split()
    C = int(C)
    # W = str(W)
    for i in range(len(W)):
        print(W[i]*C, end='')
    print()
