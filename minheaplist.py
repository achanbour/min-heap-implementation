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
        if self.min is None:
            self.min = Item(new, None, None)
            return

        head = self.min
        old = head.next

        """
        We insert the new item between the head pointer and the next item.
        """
        old.previous = new
        new.previous = head
        head.next = new
        new.next = old

        """
        In case the new item has a lower value than the head pointer, then
        the new item becomes the head pointer.
        """
        if new.value < head.value:
            self.min = new

    def minHeapify(self, n):
        lowest = n

        for c in [n.left, n.right]:
            if c is not None and c.value < lowest.value:
                lowest = c

        if lowest is n:
            return

        lowest.value, n.value = n.value, lowest.value
        self.minHeapify(n, lowest)

    """
    We are forced to traverse the whole binary tree from left to right and
    apply the minHeapify() on each traversed node.
    """
    def buildMinHeap(self, root):
        if root is None:
            return

        self.buildMinHeap(root.left)
        self.minHeapify(root)
        self.buildMinHeap(root.right)

    def linkheaps(self, h1, h2):
        node = h1

        """
        We append the second heap at the leftmost leaf of the first heap and we
        minheapify the resulting heap.
        """
        while node.left is not None:
            node = node.left
        node.left = h2

        self.buildMinHeap(h1)

    """
    Combine all the individual minheaps in the entire rootlist into a single
    big minheap.

    The former items of the rootlist are left dangling and will be deallocated
    from memory by the Python garbage collector.
    """

    def combineMinHeaps(self):

        big = Item(self.min.heap, None, None)

        item = self.min
        while item.next is not None:
            self.linkheaps(big.heap, item.next.heap)

        self.min = big

    def extractMin(self):
        head = self.min

        l, r = head.heap.left, head.heap.right

        """
        We ensure that the left item always has the lowest value.
        """
        if l.value > r.value:
            l, r = r, l

        """
        Insert the left and right sub-minheaps as items to the rootlist.
        """
        litem = Item(l, head.previous, None)
        ritem = Item(r, None, head.next)
        head.previous.next = litem
        head.next.previous = ritem

        """
        Connect the left and right items together.
        """
        ritem.previous = litem
        litem.next = ritem

        """
        Since we ensured that the left item always has the lowest value, we make
        it the new head pointer of the rootlist.

        The old head pointer is disconnected from the rootlist and removed.

        The cleanup operation is performed by calling combineMinHeaps() on the
        entire rootlist.
        """
        self.min = left
        self.combineMinHeaps()

        return head.heap.value


    def decreaseKey(self, n, k):
        pass

    def union(self, H):
        pass
