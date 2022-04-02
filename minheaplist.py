class Node:
    def __init__(self, val, le, ri, pa):
        self.value = val
        self.left = le
        self.right = ri
        self.parent = pa


class Item:
    def __init__(self, aroot, p, n):
        self.heap = aroot
        self.previous = p
        self.next = n


class MinHeaplist:
    def __init__(self):
        self.min = None

    """
    In order to make the insert() operation O(1) we ensure that each next item
    has a root value greater than the head pointer.
    """

    def insert(self, x):

        new = Node(x, None, None, None)

        """
        Trivial case when the head pointer is null.
        """
        if self.min == None:
            self.min = Item(new, None, None)
            return

        head = self.min.heap
        old = head.next

        """
        We insert the new item between the head pointer and the next item.
        """
        old.previous = new
        new.previous = head
        head.next = new
        new.next = old

        """
        In case the new item has a lower value than the head pointer then
        the new item becomes the head pointer.
        """
        if new.value < head.value:
            self.min = new


    def linkheaps(self, h1, h2):
        pass

    def extractMin(self):
        pass

    def union(self, H):
        pass

    def decreaseKey(self, node, k):
        pass
