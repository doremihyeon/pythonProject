arr = input()
count = 0

for i in arr:
    if 'a'<= i <= 'z':
        count += 1
    
    elif 'A'<= i <= 'Z':
        count += 1
print(count)