# You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero. You want to decide whether or not there is an index i such that A[i] = i. Design the fastest algorithm that you can for solving this problem.

def check_index_eq_value(lst: list[int]) -> bool:
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        return lst[0] == 0
    if len(lst) == 2:
        return lst[0] == 0 or lst[1] == 1
    m = len(lst) // 2
    if lst[m] == m:
        return True
    return check_index_eq_value(lst[m:]) if lst[m] < m else check_index_eq_value(lst[:m+1])
