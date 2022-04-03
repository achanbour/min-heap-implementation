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
