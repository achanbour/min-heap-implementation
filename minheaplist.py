#!/usr/bin/env python3
class Node:
    def __init__(self, val, le=None, ri=None, pa=None):
        self.value = val
        self.left = le
        self.right = ri
        self.parent = pa

    """
    Prints the whole tree below the current node.
    """
    def print(self):
        self.printrec()

    """
    Recursively prints the values in the tree, indenting by depth.
    """
    def printrec(self, depth=0):
        print("    " * depth, end="")  # right amount of indentation
        print(self.value)
        if self.left is None:
            print("    " * (depth + 1), "None")
        else:
            self.left.printrec(depth + 1)
        if self.right is None:
            print("    " * (depth + 1), "None")
        else:
            self.right.printrec(depth + 1)


class Item:
    def __init__(self, aroot, p=None, n=None):
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

        new = Item(Node(x))

        """
        Trivial case when the head pointer is null.
        """
        if self.min is None:
            self.min = new
            return new

        head = self.min

        """
        We insert the new item between the head pointer and the next item.
        """

        if head.next is not None:
            head.next.previous = new
            new.next = head.next
        else:
            head.previous = new
            new.next = head

        new.previous = head
        head.next = new

        """
        In case the new item has a lower value than the head pointer, then
        the new item becomes the head pointer.
        """
        if new.heap.value < head.heap.value:
            self.min = new

        return new

    """
    Removing an item with value x from the rootlist.
    """
    def remove(self, x):
        head = self.min

        if head.heap.value == x:
            head.next.previous = head.previous
            head.previous.next = head.next
            self.min = head.next

        head = self.find(x)

        if head is not None:
            head.next.previous = head.previous
            head.previous.next = head.next

    """
    Find an item with value x in the rootlist.
    """
    def find(self, x):
        head = self.min
        while head.next is not self.min:
            if head.heap.value == x:
                return head
            head = head.next

    """
    This function rebalances the tree and corrects any violation of the min-heap property.
    """

    def minHeapify(self, n):
        lowest = n

        for c in [n.left, n.right]:
            if c is not None and c.value < lowest.value:
                lowest = c

        if lowest is n:
            return

        lowest.value, n.value = n.value, lowest.value
        self.minHeapify(lowest)

    """
    We are forced to traverse the whole binary tree from left to right
    and apply the minHeapify() on each traversed node.
    """

    def buildMinheap(self, root):
        if root is None:
            return

        """
        Goes from leftmost node and applies minHeapify from left to right.
        """

        self.buildMinheap(root.left)
        self.minHeapify(root)
        self.buildMinheap(root.right)

    def linkheaps(self, h1, h2):
        node = h1

        """
        We append the second heap at the leftmost leaf of the first heap (without loss of generality)
        and we minheapify the resulting heap.
        """
        while node.left is not None:
            node = node.left
        node.left = h2
        h2.parent = node

        self.buildMinheap(h1)

    """
    Combine all the individual minheaps in the collection into a single big min-heap.

    The former items of the rootlist are left dangling and will be deallocated
    from memory by the Python garbage collector.

    This eventually amounts to them being removed from the min-heap list.
    """

    def combineMinHeaps(self):

        big = Item(self.min.heap)

        item = self.min
        while item.next is not self.min:
            self.linkheaps(big.heap, item.next.heap)
            item = item.next

        self.min = big

    def extractMin(self):

        head = self.min
        value = head.heap.value

        l, r = head.heap.left, head.heap.right

        """
        Trivial case: a singleton rootlist item.
        """
        if l is None or r is None:
            if head.next is not None and head.previous is not None:
                """
                Disconnect the min-item.
                """
                head.previous.next = head.next
                head.next.previous = head.previous

                """
                Advance head pointer by one.
                """
                self.min = head.next

            self.combineMinHeaps()
            return value

        """
        We ensure that the left item always has the lowest value.
        """
        if l.value >= r.value:
            l, r = r, l

        """
        Insert the left and right sub-minheaps as items to the rootlist.
        """
        litem = Item(l, head.previous, None)
        head.previous.next = litem

        ritem = Item(r, None, head.next)
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
        return value

    """
    Create a new min-heap item consisting of a single node n with the new
    value k and create -- if necessary -- one or two additional min-heap
    items if n has any children.
    """

    def decreaseKey(self, n, k):

        """
        Inserting the update node to the rootlist.
        """
        self.insert(k)

        """
        Attaching any min-heap rooted at a child of n into the rootlist.
        """

        node = self.find(k)

        if n.right is not None:
            node.heap.right = n.right
        elif n.left is not None:
            node.heap.left = n.left

        """
        Updating the head pointer of the rootlist.
        """

        if k < self.min.heap.value:
            head = self.find(k)
            if head is not None:
                self.min = head

        """"
        Removing node from rootlist.
        """
        if n.parent is not None and n.parent.left is not None and n.parent.left is n:
            n.parent.left = None
        elif n.parent is not None and n.parent.right is not None and n.parent.left is n:
            n.parent.right = None

        if n.parent is None:
            self.remove(n.value)

    """
    Iterate through the rootlist denoted by H and insert each item into the
    current rootlist (pointed to by self).
    """

    def union(self, H):
        item = H.min
        while item.next is not H.min:
            new = self.insert(item.heap.value)
            new.heap.left = item.heap.left
            new.heap.right = item.heap.right
            item.heap.parent = new.heap
            item = item.next

    def print(self):
        h = self.min
        if h is not None:
            print("-----")
            h.heap.printrec()
            h = h.next
            while h is not None and h is not self.min:
                print("-----")
                h.heap.printrec()
                h = h.next
            print("-----")

"""
Testing.
"""

if __name__ == '__main__':

    H = MinHeaplist()

    print("Inserting 5")
    H.insert(5)
    print("Inserting 3")
    H.insert(3)
    print("Inserting 7")
    H.insert(7)
    print("Inserting 6")
    H.insert(6)
    H.print()

    print("Extracting ",H.extractMin())

    print("The current min-heaplist:")
    H.print()

    print("Inserting 4")
    H.insert(4)

    print("The current min-heaplist:")
    H.print()

    n=H.min.next.heap.left
    print("Decreasing key",n.value,"to 2")
    H.decreaseKey(n,2)
    H.print()



