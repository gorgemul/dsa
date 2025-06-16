import math

class MaxHeap:
    def __init__(self, lst):
        self.heap = self._heapify(lst)

    def _heapify(self, lst):
        for i in range(len(lst) // 2 - 1, -1, -1):
            self._sift_down(lst, i, len(lst))
        return lst

    def _sift_down(self, lst, i, n):
        while True:
            biggest = i
            left = i*2+1
            right = i*2+2
            if left < n and right < n and lst[left] < lst[right]: # invariant of left child always smaller or euqal to parent
                lst[left], lst[right] = lst[right], lst[left]
            if left < n and lst[left] > lst[biggest]:
                lst[i], lst[left] = lst[left], lst[i]
                biggest = left
            if biggest == i: break
            i = biggest

    def dump(self):
        print_count, depth = 0, 0
        while print_count < len(self.heap):
            for i in range(print_count, print_count + 2**depth):
                if i == len(self.heap): break
                print(self.heap[i], end=", ")
            print("")
            print_count += 2**depth
            depth += 1

    def insert(self, value):
        self.heap.append(value)
        child = len(self.heap) - 1
        while True:
            parent = math.ceil(child / 2) - 1
            if parent < 0 or self.heap[parent] > self.heap[child]: return
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent

    def extract_max(self):
        if len(self.heap) == 0: return None
        current, last = 0, len(self.heap) - 1
        max_val = self.heap[current]
        self.heap[current], self.heap[last] = self.heap[last], self.heap[current]
        self.heap.pop()
        while True:
            biggest = current
            left = current*2+1
            right = current*2+2
            n = len(self.heap)
            if left < n and self.heap[left] > self.heap[biggest]:
                biggest = left
            if left < n and self.heap[right] > self.heap[biggest]:
                biggest = right
            if biggest == current: return max_val
            self.heap[biggest], self.heap[current] = self.heap[current], self.heap[biggest]
            current = biggest
