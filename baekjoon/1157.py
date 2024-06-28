word = input().lower()
arr = []
for i in range(26):
    arr.append(0)

for alpa in word:
    idx = ord(alpa) - ord("a")
    arr[idx] += 1

M = max(arr)
count = 0
for number in arr:
    if number == M:
        count += 1

# print(count)
if count >= 2:
    print("?")
else:
    max_index = arr.index(M)
    max_char = chr(max_index + ord("a")).upper()
    print(max_char)