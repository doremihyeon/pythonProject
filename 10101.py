tri = []
for i in range(3):
    t = int(input())
    tri.append(t)

if tri.count(60) == 3:
    print("Equilateral")

elif sum(tri) == 180 and len(set(tri)) == 2:
    print("Isosceles")

elif sum(tri) == 180 and len(set(tri)) == 3:
    print("Scalene")

else:
    print("Error")