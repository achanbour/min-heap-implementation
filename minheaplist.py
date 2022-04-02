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


def minHeapify(n):
    lowest = n

    for c in [n.left, n.right]:
        if c is not None and c.value < lowest.value:
            lowest = c

    if lowest is n:
        return

    lowest.value, n.value = n.value, lowest.value
    minHeapify(n, lowest)

def buildMinHeap(root):
    if root is None:
        return

    buildMinHeap(root.left)
    minHeapify(root)
    buildMinHeap(root.right)


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
        if self.min is None:
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

    def union(self, h):
        pass

    def decreaseKey(self, node, k):
        pass
