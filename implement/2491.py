# 크로아티아 알파벳

word = input()

jay = ['l', 'n']

now = len(word) - 1
count = 0

while now >= 0:
    if word[now] == '-':
        now -= 2
        count += 1
    elif word[now] == '=':
        if now-1 >= 0 and word[now-1] == 'z':
            if now-2 >= 0 and word[now-2] == 'd':
                now -= 3
            else:
                now -= 2
            count += 1
        else:
            now -= 2
            count += 1
    elif word[now] == 'j':
        if now-1 >= 0 and word[now-1] in jay:
            now -= 2
            count += 1
        else:
            now -= 1
            count += 1
    else:
        now -= 1
        count += 1

print(count)