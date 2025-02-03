# 두 용액

import sys

input = sys.stdin.readline

n = int(input().rstrip())

nums = list(map(int, input().split()))

nums.sort()

result = []
min_abs = float('inf')
start, end = 0, len(nums)-1

while start < end:
    now = nums[start] + nums[end]
    if abs(now) <= min_abs:
        min_abs = abs(now)
        result = [nums[start], nums[end]]
    if now > 0:
        end -= 1
    elif now < 0:
        start += 1
    else:
        break

print(*result)



# 1치 검색 완료(1.29)
# import sys

# input = sys.stdin.readline

# n = int(input().rstrip())

# num = list(map(int, input().split()))
# num.sort()

# start = 0
# end = len(num)-1
# result = float('inf')
# answer = []

# while start < end:
#     now = num[start] + num[end]
#     if abs(now) < abs(result):
#         result = now
#         answer = [num[start], num[end]]
#     if now < 0:
#         start += 1
#     elif now > 0:
#         end -= 1
#     else:
#         break
# print(*answer)