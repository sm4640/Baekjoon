# 회전하는 큐

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums_index = [i for i in nums]

count = 0

while nums:
    if nums_index[0] == 1:
        del nums[0]
        del nums_index[0]
        n -= 1
        for i in range(len(nums_index)):
            nums_index[i] -= 1
        continue
    rotate = (n-nums_index[0]+1) if abs(n-nums_index[0]+1) <= abs(1-nums_index[0]) else (1-nums_index[0])
    for i in range(len(nums_index)):
        nums_index[i] = nums_index[i] + rotate
        if nums_index[i] < 1:
            nums_index[i] = n + nums_index[i]
        elif nums_index[i] > n:
            nums_index[i] = nums_index[i] - n
    count += abs(rotate)

print(count)


### 첫번째랑 끝의 원소를 다 뽑을 수 있는 줄 알았다... -> 첫 번쨰 원소만 뽑을 수 있음(더 쉽죠..)
# nums_index = [i for i in nums]

# count = 0

# while nums:
#     if nums_index[0] == 1:
#         del nums[0]
#         del nums_index[0]
#         n -= 1
#         m -= 1
#         for i in range(len(nums_index)):
#             nums_index[i] -= 1
#     elif nums_index[0] == n:
#         del nums[0]
#         del nums_index[0]
#         n -= 1
#         m -= 1
#     else:
#         rotate = (n - nums_index[0]) if abs(n - nums_index[0]) <= abs(1-nums_index[0]) else (1-nums_index[0])
#         print("rotate: ", rotate)
#         print("nums_index: ", nums_index)
#         for i in range(len(nums_index)):
#             nums_index[i] = nums_index[i] + rotate
#             if nums_index[i] < 1:
#                 nums_index[i] = n + nums_index[i]
#             elif nums_index[i] > n:
#                 nums_index[i] = nums_index[i] - n
#         count += abs(rotate)

# print(count)
