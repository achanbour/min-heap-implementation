#!/usr/bin/env python3

from plotter import *
from minheaplist import *

import tests.minheaplist as test

if __name__ == "__main__":

    plotter = GraphPlotter()

    n = Node(5)
    n.left = Node(3)
    n.left.left = Node(2)
    n.left.right = Node(1)
    n.right = Node(4)

    plotter.save_img(n, "before_heapify")

    heaplist = MinHeaplist()
    heaplist.buildMinHeap(n)

    plotter.save_img(n, "after_heapify")
