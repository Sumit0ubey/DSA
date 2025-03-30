
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None

    def insert(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            self._insertRecursive(self.head, item)

    def _insertRecursive(self, current, item):
        if item < current.data:
            if current.left is None:
                current.left = Node(item)
            else:
                self._insertRecursive(current.left, item)
        else:
            if current.right is None:
                current.right = Node(item)
            else:
                self._insertRecursive(current.right, item)

    def traverse(self):
        return self._traverseInOrderRecursive(self.head)

    def _traverseInOrderRecursive(self, current):
        result = []
        if current is not None:
            result += self._traverseInOrderRecursive(current.left)
            result.append(current.data)
            result += self._traverseInOrderRecursive(current.right)
        return result


binearySearchTree = BST()
binearySearchTree.insert(5)
binearySearchTree.insert(3)
binearySearchTree.insert(7)
binearySearchTree.insert(2)
binearySearchTree.insert(4)
binearySearchTree.insert(6)
binearySearchTree.insert(8)

print(binearySearchTree.traverse())
        
