from heapq import heappush, heappop

class Median:
    def __init__(self, nums = []):
        self.max_heap = []
        self.min_heap = []
        for i in nums: self.add(i)
    def add(self, val):
        mid = float("inf") if len(self.max_heap) == 0 else abs(self.max_heap[0])
        if val <= mid:
            heappush(self.max_heap, -val)
        else:
            heappush(self.min_heap, val)
        if len(self.max_heap) - len(self.min_heap) == 2:
            heappush(self.min_heap, abs(heappop(self.max_heap)))
        elif len(self.min_heap) - len(self.max_heap) == 2:
            heappush(self.max_heap, -heappop(self.min_heap))
    def get(self):
        if len(self.min_heap) == 0 and len(self.max_heap) == 0: return None
        if len(self.max_heap) >= len(self.min_heap):
            return abs(heappop(self.max_heap))
        else:
            return heappop(self.min_heap)

if __name__ == "__main__":
    with open("number_streams.txt", "r") as file:
        nums = [int(i) for i in file]
        median = Median(nums)
        print(median.get())
