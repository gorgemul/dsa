# efficiently generate ineger inversion count for 100,000 numbers with merge sort with a time complexity of O(nlog(n))

def merge_sort_and_inversion_count(lst: list[int]) -> int:
    return merge_sort_and_inversion_count_recursive(lst, 0, len(lst) - 1)

def merge_sort_and_inversion_count_recursive(lst: list[int], l: int, r: int) -> int:
    if l >= r: return 0
    m = l + (r - l) // 2
    l_count = merge_sort_and_inversion_count_recursive(lst, l, m)
    r_count = merge_sort_and_inversion_count_recursive(lst, m + 1, r)
    split_count = merge_and_split_count(lst, l, r)
    return l_count + r_count + split_count

def merge_and_split_count(lst: list[int], l: int, r: int) -> int:
    m = l + (r - l) // 2
    count, i, j, k = 0, 0, 0, l
    l_lst = lst[l:m+1]
    r_lst = lst[m+1:r+1]
    while i < len(l_lst) and j < len(r_lst):
        if l_lst[i] < r_lst[j]:
            lst[k] = l_lst[i]
            i += 1
        else:
            lst[k] = r_lst[j]
            j += 1
            count += len(l_lst) - i
        k += 1
    while i < len(l_lst):
        lst[k] = l_lst[i]
        i += 1
        k += 1
    while j < len(r_lst):
        lst[k] = r_lst[j]
        j += 1
        k += 1
    return count

if __name__ == "__main__":
    with open("integerList.txt", "r+") as f:
        num_lst = [int(line) for line in f]
        print(merge_sort_and_inversion_count(num_lst))
