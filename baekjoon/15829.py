L = int(input())
alp = input()
answer = 0
MOD = 1234567891

for i in range(L):
    answer +=  (ord(alp[i]) - 96) * (31 ** i)
print(answer % MOD)