# AC

t = int(input())

total_lst = []

for _ in range(t):
    now = 0
    p = input()
    n = int(input())
    lst = ((input()[1:])[:-1]).split(',')
    if lst[0] == '':
        lst = []
    for i in range(len(p)):
        if p[i] == 'R':
            if now == 0:
                now = -1
            else:
                now = 0
        else:
            if lst:
                del lst[now]
            else:
                total_lst.append('error')
                break
    else:
        if now == 0:
            total_lst.append(list(map(int,lst)))
        else:
            total_lst.append(list(map(int, list(reversed(lst)))))

for i in range(len(total_lst)):
    if total_lst[i] == 'error':
        print(total_lst[i])
    else:
        print("[" + ",".join(map(str, total_lst[i])) + "]")