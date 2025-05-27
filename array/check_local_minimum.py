#You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four neighbors; numbers on the side have three; the four corners have two.) Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers. (Note: since there are n^2 numbers in the input, you cannot afford to look at all of them. Hint: Think about what types of recurrences would give you the desired upper bound.)

def check_local_minimum(grid: list[list[int]]) -> bool:
    return check_local_minimum_recursive(grid, 0, len(grid[0]) - 1, 0, len(grid) - 1)

def grid_item_local_minimum(grid: list[list[int]], row: int, column: int) -> bool:
    item = grid[row][column]
    total_row, total_column = len(grid), len(grid[0])
    left = float("inf") if column - 1 < 0 else grid[row][column - 1]
    right = float("inf") if column + 1 >= total_column else grid[row][column + 1]
    top = float("inf") if row - 1 < 0 else grid[row - 1][column]
    bottom = float("inf") if row + 1 >= total_row else grid[row + 1][column]
    return item < left and item < right and item < top and item < bottom

def check_local_minimum_recursive(grid: list[list[int]], left: int, right: int, top: int, bottom: int) -> bool:
    if left == right and top == bottom:
        return False
    mid_row, mid_col = (bottom - top) // 2, (right - left) // 2
    minimum: tuple[float, int, int] = (float("inf"), -1, -1)
    for column in range(left, right + 1):
        if grid[mid_row][column] < minimum[0]:
            minimum = (grid[mid_row][column], mid_row, column)
    for row in range(top, bottom + 1):
        if grid[row][mid_col] < minimum[0]:
            minimum = (grid[row][mid_col], row, mid_col)
    _, row, column = minimum
    smaller_than_left = True if column == left else grid[row][column] < grid[row][column - 1]
    if not smaller_than_left:
        if grid_item_local_minimum(grid, row, column - 1):
            return True
        # second or third quadrant
        return check_local_minimum_recursive(grid, left, mid_col - 1, top, mid_row - 1) if row < mid_row else check_local_minimum_recursive(grid, left, mid_col - 1, mid_row + 1, bottom)
    smaller_than_right = True if column == right else grid[row][column] < grid[row][column + 1]
    if not smaller_than_right:
        if grid_item_local_minimum(grid, row, column + 1):
            return True
        # first or four quadrant
        return check_local_minimum_recursive(grid, mid_col + 1, right, top, mid_row - 1) if row < mid_row else check_local_minimum_recursive(grid, mid_col + 1, right, mid_row + 1, bottom)
    smaller_than_top = True if row == top else grid[row][column] < grid[row - 1][column]
    if not smaller_than_top:
        if grid_item_local_minimum(grid, row - 1, column):
            return True
        # second or first quadrant
        return check_local_minimum_recursive(grid, left, mid_col - 1, top, mid_row - 1) if column < mid_col else check_local_minimum_recursive(grid, mid_col + 1, right, top, mid_row - 1)
    smaller_than_bottom = True if row == bottom else grid[row][column] < grid[row + 1][column]
    if not smaller_than_bottom:
        if grid_item_local_minimum(grid, row + 1, column):
            return True
        # third or four quadrant
        return check_local_minimum_recursive(grid, left, mid_col - 1, mid_row + 1, bottom) if column < mid_col else check_local_minimum_recursive(grid, mid_col + 1, right, mid_row + 1, bottom)
    return True
