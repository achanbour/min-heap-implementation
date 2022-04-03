#!/usr/bin/env python3

from minheaplist import *
from copy import *


def equalsTree(r1, r2):
    if r1 is None and r2 is None:
        return True

    if r1 is not None and r2 is not None:
        return (
            (r1.value == r2.value)
            and equalsTree(r1.left, r2.left)
            and equalsTree(r1.right, r2.right)
        )

    return False


def test_equalsTree():

    r1 = Node(1)
    r1.left = Node(3)
    r1.left.left = Node(5)
    r1.left.left.left = Node(14)
    r1.left.right = Node(7)
    r1.right = Node(4)
    r1.right.left = Node(8)
    r1.right.left.right = Node(17)
    r1.right.right = Node(11)

    r2 = deepcopy(r1)

    if equalsTree(r1, r2):
        print("equalsTree passed the test")
    else:
        print("equalsTree failed the test")





def equalsMinHeaplist(h1, h2):

    i1, i2 = h1.min, h2.min

    while i1.next is not h1.min and i2.next is not h2.min:
        if not equalsTree(i1.heap, i2.heap):
            return False
        i1 = i1.next
        i2 = i2.next

    if i1.next is not h1.min or i2.next is not h2.min:
        return False

    return True


if __name__ == "__main__":
    test_equalsTree()
