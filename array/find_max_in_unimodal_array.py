# You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, after which its elements are in decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.

def find_max(unimodal_lst: list[int]) -> int | None:
    if len(unimodal_lst) == 0:
        return None
    if len(unimodal_lst) == 1:
        return unimodal_lst[0]
    if (len(unimodal_lst) == 2):
        return max(unimodal_lst[0], unimodal_lst[1])
    m = len(unimodal_lst) // 2
    left, mid, right = unimodal_lst[m-1], unimodal_lst[m], unimodal_lst[m+1]
    if left < mid and mid > right:
        return mid
    elif left > mid and mid > right:
        return find_max(unimodal_lst[:m+1])
    elif left < mid and mid < right:
        return find_max(unimodal_lst[m:])
