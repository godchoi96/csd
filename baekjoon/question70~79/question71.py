# 71. 부녀회장이 됥테야
# https://www.acmicpc.net/problem/2775

# 4층의 3호
# (3층의 1호) + (3층의 2호) + (3층의 3호)
# = (2층의 1호) + (2층의 1호 + 2층의 2호) + (2층의 1호 + 2층의 2호 + 2층의 3호)
# = (1층의 1호) + (1층의 1호 + 1층의 1호 + 1층의 2호) + (1층의 1호 + 1층의 1호 + 1층의 2호 + 1층의 1호 + 1층의 2호 + 1층의 3호)
# = (0층의 1호) + (0층의 1호 + 0층의 1호 + 0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 2호 + 0층의 3호)
# = 1 * 1 + (1 * 3 + 2 * 1) + (1 * 6 + 2 * 3 + 3 * 1)

# 3층의 4호
# (2층의 1호) + (2층의 2호) + (2층의 3호) + (2층의 4호)
# = (1층의 1호) + (1층의 1호 + 1층의 2호) + (1층의 1호 + 1층의 2호 + 1층의 3호) + (1층의 1호 + 1층의 2호 + 1층의 3호 + 1층의 4호)
# = (0층의 1호) + (0층의 1호 + 0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 2호 + 0층의 3호) + (0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 2호 + 0층의 3호 + 0층의 1호 + 0층의 2호 + 0층의 3호 + 0층의 4호)

# 3층의 3호
# (2층의 1호) + (2층의 2호) + (2층의 3호)
# = (1층의 1호) + (1층의 1호 + 1층의 2호) + (1층의 1호 + 1층의 2호 + 1층의 3호)
# = (0층의 1호) + (0층의 1호 + 0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 2호 + 0층의 3호)
# = (6 * 0층의 1호) + (3 * 0층의 2호) + (1 * 0층의 3호) = 6 + 6 + 3 = 15

# 2층의 4호
# (1층의 1호) + (1층의 2호) + (1층의 3호) + (1층의 4호)
# = (0층의 1호) + (0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 2호 + 0층의 3호) + (0층의 1호 + 0층의 2호 + 0층의 3호 + 0층의 4호)
# = (4 * 0층의 1호) + (3 * 0층의 2호) + (2 * 0층의 3호) + (1 * 0층의 4호) = 4 + 6 + 6 + 4 = 20

# 2층의 3호
# (1층의 1호) + (1층의 2호) + (1층의 3호)
# = (0층의 1호) + (0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 2호 + 0층의 3호)
# = (3 * 0층의 1호) + (2 * 0층의 2호) + (1 * 0층의 3호) = 3 + 4 + 3 = 10

# 3층의 3호
# (2층의 1호) + (2층의 2호) + (2층의 3호)
# = (1층의 1호) + (1층의 1호 + 1층의 2호) + (1층의 1호 + 1층의 2호 + 1층의 3호)
# = (0층의 1호) + (0층의 1호 + 0층의 1호 + 0층의 2호) + (0층의 1호 + 0층의 1호 + 0층의 2호 + 0층의 1호 + 0층의 2호 + 0층의 3호)
# = (6 * 0층의 1호) + (3 * 0층의 2호) + (1 * 0층의 3호) = 6 + 6 + 3 = 15

# 3, 3
# 2: 1, 2, 3 > 1: 1, 1, 2, 1, 2, 3 > 0: 1, 1, 1, 2, 1, 1, 2, 1, 2, 3
