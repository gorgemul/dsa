# You are given as input an unsorted array of n distinct numbers, where n is a power of 2. Give an algorithm that identifies the second-largest number in the array, and that uses at most n + logn - 2 comparisions

class BstTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        if self.value == value:
            return
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BstTreeNode(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BstTreeNode(value)
       
    def get_second_biggest_number(self) -> int | None:
        if self.right is None:
            return None
        if self.right.right is None:
            return self.value
        return self.right.get_second_biggest_number()
