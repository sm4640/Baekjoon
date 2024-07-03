# 사탕게임

n = int(input())

board = [list(input()) for _ in range(n)]

def find_row(r):
    longest = 1
    now = board[r][0]
    now_length = 1
    for i in range(1,n):
        if board[r][i] == now:
            now_length += 1
        else:
            longest = max(longest, now_length)
            now = board[r][i]
            now_length = 1
    longest = max(longest, now_length)
    return longest

def find_col(c):
    longest = 1
    now = board[0][c]
    now_length = 1
    for i in range(1,n):
        if board[i][c] == now:
            now_length += 1
        else:
            longest = max(longest, now_length)
            now = board[i][c]
            now_length = 1
    longest = max(longest, now_length)
    return longest

whole_longest = max(max([find_row(x) for x in range(n)]), max([find_col(x) for x in range(n)]))

# 가로로 바꾸기
for r in range(n):
    for c in range(n-1):
        board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
        whole_longest = max(whole_longest, find_row(r), find_col(c), find_col(c+1))
        board[r][c], board[r][c+1] = board[r][c+1], board[r][c]

# 세로로 바꾸기
for c in range(n):
    for r in range(n-1):
        board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
        whole_longest = max(whole_longest, find_row(r), find_row(r+1), find_col(c))
        board[r][c], board[r+1][c] = board[r+1][c], board[r][c]

print(whole_longest)