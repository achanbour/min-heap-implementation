#!/usr/bin/env python3

from minheaplist import *
from copy import *


def equalsTree(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return (
            (a.value == b.value)
            and equalsTree(a.left, b.left)
            and equalsTree(a.right, b.right)
        )
    return False


def test_equalsTree():

    a = Node(1)
    a.left = Node(3)
    a.left.left = Node(5)
    a.left.left.left = Node(14)
    a.left.right = Node(7)
    a.right = Node(4)
    a.right.left = Node(8)
    a.right.left.right = Node(17)
    a.right.right = Node(11)

    b = deepcopy(a)

    if equalsTree(a,b):
        print("equalsTree passed the test")
    else:
        print("equalsTree failed the test")

if __name__ == "__main__":
     test_equalsTree()
