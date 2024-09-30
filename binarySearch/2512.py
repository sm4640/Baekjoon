# 예산

n = int(input())

budgets = list(map(int, input().split()))

m = int(input())

start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for budget in budgets:
        if budget <= mid:
            total += budget
        else:
            total += mid
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)