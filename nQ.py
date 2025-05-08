n = 4
board = [[0]*n for _ in range(n)]
pos = {}

def is_safe(r, c):
    for i in range(r):
        if board[i][c] or (c - r + i >= 0 and board[i][c - r + i]) or (c + r - i < n and board[i][c + r - i]):
            return False
    return True

def solve(r=0):
    if r == n:
        return True
    for c in range(n):
        if is_safe(r, c):
            board[r][c] = 1
            pos[r] = c
            if solve(r + 1):
                return True
            board[r][c] = 0
    return False

solve()
print("Matrix:")
for row in board:
    print(row)
print("Positions:", pos)
