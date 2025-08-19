str = input()
result = ""

for i in str:
    if 'A'<= i <= 'Z':
        result += chr(ord(i)+32)
    else:
        result += chr(ord(i)-32)

print(result)