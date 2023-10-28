#!/usr/bin/env python3

from plotter import *
from minheaplist import *

import tests.minheaplist as test

if __name__ == "__main__":

    plotter = GraphPlotter()

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
    heaplist.buildMinHeap(n)

    plotter.save_img(n, "after_heapify")
