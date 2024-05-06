# 설탕 배달

n = int(input())

dp = []

five = n//5
three = (n - (five*5))//3

while five >= 0:
    if (five*5) + (three*3) == n:
        dp.append(five+three)
    five -= 1
    three = (n - (five*5))//3

if not dp:
    print(-1)
else:
    print(min(dp))