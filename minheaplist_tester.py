class Node:
    def __init__(self,val,le,ri,pa):
        self.value = val
        self.left=le
        self.right=ri
        self.parent=pa

    # prints the whole tree below the current node
    def print(self):
        self.printrec(0)

    # recursively prints the values in the tree, indenting by depth
    def printrec(self,depth):
        print("    "*depth,end = "") # right amount of indentation
        print(self.value)
        if self.left==None:
            print("    "*(depth+1),"None")
        else:
            self.left.printrec(depth+1)
        if self.right==None:
            print("    "*(depth+1),"None")
        else:
            self.right.printrec(depth+1)

class Item:
    def __init__(self,aroot,p,n):
        self.heap=aroot
        self.previous=p
        self.next=n

class MinHeaplist:
    def __init__(self):
        self.min = None

    def insert(self,x):
        pass

    def linkheaps(self,h1,h2):
        pass

    def extractMin(self):
        pass

    def union(self,H):
        pass

    def decreaseKey(self,node,k):
        pass


    def my_print(self):
        h=self.min
        if h != None:
            print("-----")
            h.heap.print_tree()
            h = h.next
            while h != self.min:
                print("-----")
                h.heap.print_tree()
                h = h.next
            print("-----")



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
    H.my_print()

    print("Inserting 4")
    H.insert(4)

    print("The current min-heaplist:")
    H.my_print()

    n=H.min.next.heap.left
    print(n.value)
    print("Decreasing key",n.value,"to 2")
    H.decreaseKey(n,2)
    H.my_print()



# The output produced:
# Inserting 5
# Inserting 3
# Inserting 7
# Inserting 6
# -----
# 3
#      None
#      None
# -----
# 6
#      None
#      None
# -----
# 7
#      None
#      None
# -----
# 5
#      None
#      None
# -----
# Extracting  3
# The current min-heaplist:
# -----
# 5
#     6
#         7
#              None
#              None
#          None
#      None
# -----
# Inserting 4
# The current min-heaplist:
# -----
# 4
#      None
#      None
# -----
# 5
#     6
#         7
#              None
#              None
#          None
#      None
# -----
# Decreasing key 6  2
# -----
# 2
#     7
#          None
#          None
#      None
# -----
# 5
#      None
#      None
# -----
# 4
#      None
#      None
# -----
#
