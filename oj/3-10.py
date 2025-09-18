N = int(input())
num = list(map(int, input().split()))

# 중복 제거 + 내림차순 정렬
unique_nums = sorted(set(num), reverse=True)

if len(unique_nums) >= 2:
    print(unique_nums[1]) 