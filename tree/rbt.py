BLACK = "BLACK"
RED = "RED"
NIL = "NIL"

class RBTNode:
    def __init__(self, val, parent = None, color = BLACK):
        self.val = val
        self.parent = parent
        self.color = color
        self.left = None if val == NIL else RBTNode(NIL, self)
        self.right = None if val == NIL else RBTNode(NIL, self)
    def dump(self, level=0, prefix="root"):
        print(f"{'\033[30m' if self.color == BLACK else '\033[31m'}{4 * level * " "}{prefix}-{self.val}{'\033[0m'}")
        if self.left: self.left.dump(level+1, prefix="l")
        if self.right: self.right.dump(level+1, prefix="r")
    def search(self, val):
        if self.val == NIL: return None
        if val == self.val: return self
        if val < self.val: return self.left.search(val)
        if val > self.val: return self.right.search(val)
    def _left_rotation(self, parent, right_child):
        left_child, left_grandson, right_grandson = parent.left, right_child.left, right_child.right
        right_child.val, parent.val = parent.val, right_child.val
        parent.left, parent.right, right_grandson.parent = right_child, right_grandson, parent
        right_child.left, right_child.right, left_child.parent = left_child, left_grandson, right_child
    def _right_rotation(self, parent, left_child):
        right_child, left_grandson, right_grandson = parent.right, left_child.left, left_child.right
        left_child.val, parent.val = parent.val, left_child.val
        parent.left, parent.right, left_grandson.parent = left_grandson, left_child, parent
        left_child.left, left_child.right, right_child.parent = right_grandson, right_child, left_child
    def _find_pred(self, val, first=True):
        if first:
            node = self.search(val)
            if not node or node.left.val == NIL: return None
            return node.left._find_pred(val, False)
        else:
            if self.val == NIL: return self.parent
            return self.right._find_pred(val, False)
    def insert(self, val):
        if val == self.val: return # only support distinct value
        if self.val == NIL:
            self.val = val
            self.color = RED
            self.left = RBTNode(NIL, self)
            self.right = RBTNode(NIL, self)
            self._fix()
            return
        elif val < self.val:
            self.left.insert(val)
        elif val > self.val:
            self.right.insert(val)
    def delete(self, val):
        if val < self.val:
            self.left = self.left.delete(val)
        elif val > self.val:
            self.right = self.right.delete(val)
        else:
            if self.left.val == NIL and self.right.val == NIL: return RBTNode(NIL, self)
            if self.left.val != NIL and self.right.val == NIL:
                self.left.parent = self
                return self.left
            if self.left.val == NIL and self.right.val != NIL:
                self.right.parent = self
                return self.right
            pred = self._find_pred(self.val)
            if pred:
                self.val, pred.val = pred.val, self.val
                self.left = self.left.delete(val)
        return self

    def _triangle_case(self, grandparent, parent):
        return (grandparent.left.val == parent.val and parent.right.val == self.val) or (grandparent.right.val == parent.val and parent.left.val == self.val)
    def _fix(self):
        parent = self.parent
        if not parent or parent.color == BLACK: return
        grandparent = parent.parent
        uncle = grandparent.left if grandparent.left.val != parent.val else grandparent.right
        if uncle.color == RED:
            parent.color = uncle.color = BLACK
            grandparent.color = RED if grandparent.color == BLACK else RED
            if not grandparent.parent: grandparent.color = BLACK
            grandparent._fix()
            return
        if self._triangle_case(grandparent, parent):
            if parent.left.val == self.val:
                self._right_rotation(parent, self)
            else:
                self._left_rotation(parent, self)
        else: # line case 
            if grandparent.left.val == parent.val:
                self._right_rotation(grandparent, parent)
            else:
                self._left_rotation(grandparent, parent)
        self._fix()

tree = RBTNode(10)
tree.insert(5)
tree.insert(15)
tree.insert(1)
tree.insert(4)
tree.insert(14)
tree.insert(16)
tree.delete(4)
tree.dump()

"""
        10
    4      15
  1   5  14   16
"""
