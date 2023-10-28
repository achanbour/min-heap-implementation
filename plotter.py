import collections
import pydot


class GraphPlotter:
    def __init__(self):
        self.graph = None

    def traverse_inorder(self, node):
        if node is None or self.graph is None:
            return

        self.graph.add_node(pydot.Node(id(node.value), label=node.value))

        self.traverse_inorder(node.left)
        if node.left is not None:
            self.graph.add_edge(pydot.Edge(id(node.value), id(node.left.value)))
        if node.right is not None:
            self.graph.add_edge(pydot.Edge(id(node.value), id(node.right.value)))
        self.traverse_inorder(node.right)

    def save_img(self, root, name):
        self.graph = pydot.Dot(graph_type="graph")
        self.traverse_inorder(root)
        self.graph.write_png(f"{name}.png")
