# 제곱수의 합

n = int(input())

dp = [1000 for _ in range(n+1)]
dp[0] = 0

for i in range(1,n+1):
    for j in range(int(i**0.5),0,-1):
        dp[i] = min(dp[i], 1+dp[i-(j**2)])

print(dp[-1])



# 1차 풀이(테케만 다 맞음 12가 걸림)

# import math

# n = int(input())

# dp = [0,1]

# for i in range(2, n+1):
#     if int(math.sqrt(i)) == math.sqrt(i):
#         dp.append(1)
#     else:
#         dp.append(1+dp[i - (int(math.sqrt(i)))**2])

# print(dp[-1])