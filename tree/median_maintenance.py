"""
odd: n / 2
even: n / 2 -1
if len max_heap >= min_heap:
    return max in max_heap
else:
    return min in min_heap
diff of two heap can only be 1
"""
import heapq

nums = [20,10,50,25,99,17,14,5,8,19]

def median_maintenance(nums):
    min_heap = []
    max_heap = []
    for num in nums:
        
