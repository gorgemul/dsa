import random

def random_selection(lst: list[int], x) -> int | None:
    return random_selection_recursive(lst, x, 0, len(lst)-1)

def random_selection_recursive(lst: list[int], x, l, r) -> int | None:
    if x > len(lst):
        return None
    if r == l:
        return lst[l]
    pivot_index = random.randrange(l, r+1)
    lst[l], lst[pivot_index] = lst[pivot_index], lst[l]
    pivot = lst[l]
    i = l + 1
    for j in range(i, r+1):
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    exist_item_samller_than_pivot = l != i - 1
    if exist_item_samller_than_pivot:
        lst[l], lst[i-1] = lst[i-1], lst[l]
    absolute_x = x + l
    if i == absolute_x:
        return lst[i-1]
    return random_selection_recursive(lst, absolute_x - i, i, r) if absolute_x > i else random_selection_recursive(lst, x, l, i-2)
