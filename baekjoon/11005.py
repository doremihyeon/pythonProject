N, B = map(int, input().split()) 

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while N != 0:
    answer += str(num[N % B])
    N = N // B

print(answer[::-1])