#!/usr/bin/env python3

from plotter import *
from minheaplist import *

import tests.minheaplist as test

if __name__ == "__main__":
    plotter = GraphPlotter()

    """
    n = Node(19)
    n.left = Node(3)
    n.left.left = Node(5)
    n.left.left.left = Node(14)
    n.left.right = Node(7)
    n.right = Node(15)
    n.right.left = Node(8)
    n.right.left.right = Node(17)
    n.right.right = Node(11)

    plotter.save_img(n, "before_heapify")

    heaplist = MinHeaplist()
    heaplist.buildMinheap(n)

    plotter.save_img(n, "after_heapify")
    """

    L = MinHeaplist()
    L.insert(10)
    L.insert(7)
    L.insert(3)
    L.insert(14)
    L.insert(5)
    print("Printing L before the decrease key")
    L.print()

    print("Decreasing:",L.min.next.next.heap.value," to :",2)
    L.decreaseKey(L.min.next.next.heap,2)
    print("After DecreaseKey")
    L.print()


    K = MinHeaplist()
    K.insert(12)
    K.insert(4)
    K.insert(8)
    K.insert(18)
    print("Printing K")
    K.print()

    L.union(K)
    print("Printing the union")
    L.print()
    print("Extracting min value:",L.extractMin())
    L.print()
    print("Extracting min value:",L.extractMin())
    L.print()
    print("Extracting min value:",L.extractMin())
    L.print()
    extract = L.min.heap.left.left
    print("We're decreasing:",extract.value,"to 3")
    L.decreaseKey(extract,3)
    L.print()
    print("Extracting min value:",L.extractMin())
    print("Extracting min value:",L.extractMin())
    print("Extracting min value:",L.extractMin())
    L.print()

