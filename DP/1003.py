# 피보나치 함수

t = int(input())

for i in range(t):
    n = int(input())
    fibo = [(1,0),(0,1)]
    for j in range(2,n+1):
        fibo.append((fibo[j-1][0]+fibo[j-2][0], fibo[j-1][1]+fibo[j-2][1]))
    print(fibo[n][0], fibo[n][1])