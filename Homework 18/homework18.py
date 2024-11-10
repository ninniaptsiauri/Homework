class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def printParents(self):
        print('The parents of each node are: ')
        self._printParents(self.root, None)


    def _printParents(self, node, parentNode):
        if node is not None:
            if parentNode is None:
                print(node.key, '-> Root')
            else:
                print(node.key, '->', parentNode.key)

            self._printParents(node.left, node)
            self._printParents(node.right, node)



    def printLeafNodes(self):
        print('Leaf nodes are: ')
        self._printLeafNodes(self.root)


    def _printLeafNodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.key)

            self._printLeafNodes(node.left)
            self._printLeafNodes(node.right)



    def countEdges(self):
        edge_count = self._countEdges(self.root)
        print(f'The number of edges in the tree is: {edge_count}')


    def _countEdges(self, node):
        if node is None:
            return 0
        
        left_edges = self._countEdges(node.left)
        right_edges = self._countEdges(node.right)
        return left_edges + right_edges + 1

    
    
tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(14)
tree.insert(16)
tree.insert(9)
tree.insert(4)

tree.printParents()
tree.printLeafNodes()
tree.countEdges()
