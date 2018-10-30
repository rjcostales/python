BOARD_SIZE = 8


# (col, queens) What is their meaning? What do I need to write it this field?
def under_attack(col, queens):
    left = right = col
    # What does reversed means in this loop? For what reson do we need r and c (their meaning is 0 by default?)?
    for r, c in reversed(queens):
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]
    # For what reasons do we need to write smaller_solutions?
    smaller_solutions = solve(n - 1)
    return [solution + [(n, i + 1)]  # What is solution (is it a function or what?)? What is value of i?
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)
