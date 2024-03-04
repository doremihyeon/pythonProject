a, b, c, d, e = list(map(int, input().split()))
A = a ** 2
B = b ** 2
C = c ** 2
D = d ** 2
E = e ** 2
value = (A + B + C + D + E) % 10
print(value)
#반복문으로 다시 만들어보기