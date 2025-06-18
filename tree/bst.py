class Node:
    def __init__(self, val):
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None
    def dump(self, level=0, prefix="root-"):
        print(f"{4 * level * " "}{prefix}{self.val}")
        if self.left: self.left.dump(level+1, prefix="l-")
        if self.right: self.right.dump(level+1, prefix="r-")
    def search(self, val):
        if self.val == val: return self
        if val > self.val and self.right:
            return self.right.search(val)
        if val < self.val and self.left:
            return self.left.search(val)
        return None
    def insert(self, val):
        if val == self.val:
            new_node = Node(val)
            new_node.left = self.left
            self.left = new_node
        elif val > self.val:
            if not self.right:
                new_node = Node(val)
                self.right = new_node
                return
            self.right.insert(val)
        else:
            if not self.left:
                new_node = Node(val)
                self.left = new_node
                return
            self.left.insert(val)
    def traverse_dump(self):
        if self.left: self.left.traverse_dump()
        print(self.val, end=" ")
        if self.right: self.right.traverse_dump()
    def get_min(self):
        if not self.left: return self
        return self.left.get_min()
    def get_max(self):
        if not self.right: return self
        return self.right.get_max()
    def find_succ(self, val, first=True):
        if first:
            node = self.search(val)
            if not node or not self.right: return None
            return self.right.find_succ(val, False)
        else:
            if not self.left: return self
            return self.left.find_succ(val, False)
    def find_pred(self, val, first=True):
        if first:
            node = self.search(val)
            if not node or not self.left: return None
            return self.left.find_pred(val, False)
        else:
            if not self.right: return self
            return self.right.find_pred(val, False)
    def delete(self, val):
        if val < self.val:
            if self.left: self.left = self.left.delete(val)
        elif val > self.val:
            if self.right: self.right = self.right.delete(val)
        else:
            if not self.left and not self.right: return None
            if self.left and not self.right: return self.left
            if self.right and not self.left: return self.right
            pred = self.find_pred(self.val)
            if pred and self.left:
                self.val, pred.val = pred.val, self.val
                self.left = self.left.delete(val)
        return self
    def left_rotation(self, parent_val, right_child_val):
        parent, right_child = self.search(parent_val), self.search(right_child_val)
        if not parent or not right_child: return
        left_child = parent.left
        left_grandson = right_child.left
        right_grandson = right_child.right
        parent.val, right_child.val = right_child.val, parent.val
        parent.left = right_child
        parent.right = right_grandson
        right_child.left = left_child
        right_child.right = left_grandson
    def right_rotation(self, parent_val, left_child_val):
        parent, left_child = self.search(parent_val), self.search(left_child_val)
        if not parent or not left_child: return
        right_child = parent.right
        left_grandson = left_child.left
        right_grandson = left_child.right
        parent.val, left_child.val = left_child.val, parent.val
        parent.right = left_child
        parent.left = left_grandson
        left_child.left = right_grandson
        left_child.right = right_child
            
def build_bst(lst: list[int]) -> Node | None:
    copy_lst = lst[:]
    copy_lst.sort()
    return build_bst_recursive(copy_lst)
    
def build_bst_recursive(lst: list[int]) -> Node | None:
    if len(lst) == 0: return None
    m = len(lst) // 2
    root = Node(lst[m])
    root.left = build_bst_recursive(lst[:m])
    root.right = build_bst_recursive(lst[m+1:])
    return root

def main():
    root = build_bst([10,5,4,8,7,20,15,13,12,18,19,50,25,21])
    if not root: return
    root.right_rotation(8, 5)
    root.dump()

if __name__ == "__main__":
    main()
