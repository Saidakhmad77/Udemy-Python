def count_captured_pieces(board):
    n = len(board)
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def can_capture(x, y):
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny) and board[nx][ny] == 'H':
                return True
        return False

    total_captured = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X' and can_capture(i, j):
                total_captured += 1

    return total_captured

# Read input
num_test_cases = int(input())
for case in range(1, num_test_cases + 1):
    n = int(input())
    board = [input().split() for _ in range(n)]
    result = count_captured_pieces(board)
    print(f"#{case} {result}")
