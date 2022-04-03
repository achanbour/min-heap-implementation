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

        new = Item(Node(x, None, None, None), None, None)

        """
        Trivial case when the head pointer is null.
        """
        if self.min is None:
            self.min = new
            return new

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

        return new

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
        while item.next is not self.min:
            self.linkheaps(big.heap, item.next.heap)
            item = item.next

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
        self.min = litem
        self.combineMinHeaps()

        return head.heap.value

    """
    Create a new min-heap item consisting of a single node n with the new
    value k and create -- if necessary -- one or two additional min-heap
    items if n has any children.
    """

    def decreaseKey(self, n, k):

        parent = n.parent

        if n is parent.left:
            parent.left = None
        elif n is parent.right:
            parent.right = None

        """
        Create two new min-heap items and connect their respective left and
        right children -- if any -- to the new item min-heap node.
        """

        litem = self.insert(n.left.value)
        litem.heap.left = n.left.left
        litem.heap.right = n.left.right

        ritem = self.insert(n.right.value)
        ritem.heap.left = n.right.left
        ritem.heap.right = n.right.right

        """
        Remove the children of node n.
        """
        n.left = None
        n.right = None

        """
        Insert a new item with value k.
        """
        self.insert(k)

    """
    Iterate through the rootlist denoted by H and insert each item into the
    current rootlist.
    """

    def union(self, H):
        item = H.min
        while item.next is not H.min:
            new = self.insert(item.heap.value)
            new.heap.left = item.heap.left
            new.heap.right = item.heap.right
            item = item.next



