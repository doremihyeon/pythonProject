N = sorted(map(int,input().split()))
res = N[0] + N[1] + min(N[2], N[0]+N[1]-1)
print(res)