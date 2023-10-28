#!/usr/bin/env python3

from minheaplist import *

import copy
import pydot
import tests.helpers as helper


def equalsTree():

    r1 = Node(1)
    r1.left = Node(3)
    r1.left.left = Node(5)
    r1.left.left.left = Node(14)
    r1.left.right = Node(7)
    r1.right = Node(4)
    r1.right.left = Node(8)
    r1.right.left.right = Node(17)
    r1.right.right = Node(11)

    r2 = copy.deepcopy(r1)

    if helper.equalsTree(r1, r2):
        print("equalsTree passed the test")
    else:
        print("equalsTree failed the test")


def equalsMinHeaplist():
    pass


def minHeapify():
    pass


