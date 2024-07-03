# 치킨 배달
import itertools
import copy

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
chicken_dist = []
chicken_sum = []

result = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i+1,j+1))
        elif city[i][j] == 2:
            chicken.append((i+1,j+1))

for i in home:
    lst = []
    for j in chicken:
        lst.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
    chicken_dist.append(lst)

com = list(itertools.combinations([x for x in range(len(chicken))], m))

for c in com:
    chicken_validated_index = [x for x in c]
    tmp = copy.deepcopy(chicken_dist)
    k = 0
    for i in range(len(home)):
        while 1:
            if tmp[i].index(min(tmp[i])) in chicken_validated_index:
                k += min(tmp[i])
                break
            else:
                tmp[i][tmp[i].index(min(tmp[i]))] = 10000
    result.append(k)

print(min(result))