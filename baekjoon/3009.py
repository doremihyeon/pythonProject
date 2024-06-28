x_point = []
y_point = []

for i in range(3):
    x, y = map(int, input().split())
    x_point.append(x)
    y_point.append(y)

for j in range(3):
    if x_point.count(x_point[j]) == 1:
        x = x_point[j]
    if y_point.count(y_point[j]) == 1:
        y = y_point[j]

print(x, y)