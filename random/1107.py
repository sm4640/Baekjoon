# 리모컨

b = ['0','1','2','3','4','5','6','7','8','9']
n = int(input())
m = int(input())
if m:
    no = input().split()


base_count = abs(n - 100)
count = 1000000
lst = []

now_n = n

for i in range(m):
    b.remove(no[i])

while now_n >= 0:
    str_now_n = str(now_n)
    if all(num in b for num in list(str_now_n)):
        count = min(len(str_now_n) + n - now_n, count)
        break
    else:
        now_n -= 1

now_n = n

while now_n >= 0:
    if len(str_now_n) + now_n - n > count:
        break
    str_now_n = str(now_n)
    if all(num in b for num in list(str_now_n)):
        count = min(len(str_now_n) + now_n - n, count)
        break
    else:
        now_n += 1

print(min(base_count, count))
