char = input().strip()
text = input()
count = 0

for i in range(len(char)):
    if char[i] == text:
        count += 1

print(count)