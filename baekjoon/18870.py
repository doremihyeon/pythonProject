N = int(input())
x = list(map(int,input().split()))

X = sorted(set(x))

result = []

for i in X:
    result.append(i)

print(result)
    