import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

# 산술평균
total = sum(nums)
arth = round(total / N)

# 중앙값
sort_nums = sorted(nums)
mdn = sort_nums[N // 2]

# 최빈값
freq = Counter(nums)
max_count = max(freq.values())
candidates = []

for num, cnt in freq.items():
    if cnt == max_count:
        candidates.append(num)

candidates.sort()
if len(candidates) > 1:
    mode = candidates[1]
else:
    mode = candidates[0]

# 범위
rng = max(nums) - min(nums)

# 출력
print(arth)
print(mdn)
print(mode)
print(rng)