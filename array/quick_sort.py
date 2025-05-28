def quick_sort(lst: list[int]):
    quick_sort_recursive(lst, 0, len(lst) - 1)

def quick_sort_recursive(lst: list[int], l: int, r: int):
    if l >= r:
        return
    pivot = lst[l]
    i = l + 1
    for j in range(i, r + 1):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    exist_item_smaller_than_pivot = not i - 1 == l
    if exist_item_smaller_than_pivot:
        lst[l], lst[i-1] = lst[i-1], lst[l]
    quick_sort_recursive(lst, l, i - 2)
    quick_sort_recursive(lst, i, r)

if __name__ == "__main__":
    with open("quick_sort_integerList.txt", "r+") as f:
        num_lst = [int(line) for line in f]
        quick_sort(num_lst)
        print(num_lst)
