arr = input()
count = 0
for i in arr:
    if '0' <= i <= '9':
        count += 1
    
    else:
        continue

print(count)