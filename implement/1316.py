# 그룹 단어 체크

n = int(input())

count = 0
for j in range(n):
    word = input()
    used_alp = {}
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            if used_alp.get(word[i-1], 0):
                break
            else:
                used_alp[word[i-1]] = 1
        if i == len(word)-1:
            if used_alp.get(word[i], 0):
                break
    else:
        count += 1

print(count)