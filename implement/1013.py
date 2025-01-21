# Contact

# 1차 검색하면서 이전 방식 보완해서 해결 성공(4배 빠름)
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input().rstrip()
    while s:
        if s.find('100') == 0:
            s = s[3:]
            start1 = s.find('1')
            if start1 != -1:
                s = s[start1+1:]
            else:
                print("NO")
                break
            start0 = s.find('0')
            if start0 != -1:
                if s[start0:].startswith('01'):
                    s = s[start0:]
                else:
                    if start0 != 0:
                        s = s[start0-1:]
                    else:
                        print("NO")
                        break
            else:
                s = ''
                continue
        elif s.find('01') == 0:
            s = s[2:]
            continue
        else:
            print("NO")
            break
    else:
        print("YES")





# 1차 검색 완료(1.21)
# import sys
# import re

# input = sys.stdin.readline

# t = int(input().rstrip())

# p = re.compile('(100+1+|01)+')

# for i in range(t):
#     if p.fullmatch(input().rstrip()):
#         print('YES')
#     else:
#         print('NO')