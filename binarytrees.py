from AVLtrees import AVL

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def insert_iter(self, data: list[int]):
        """
        Create a new binary tree from a list of values.
        AVL will be used to balance the tree after each insertion, ensuring that the tree remains balanced and efficient for search operations.
        """

        newTree = AVL()
        for val in data:
            newTree.insert(val)
        
        self.root = newTree.root
        return self
    
    def preorder_traversal(self):
        return self._preorder_recursive(self.root)
    
    def _preorder_recursive(self, node):
        result = []
        if node:
            result.append(node.data)
            result.extend(self._preorder_recursive(node.left))
            result.extend(self._preorder_recursive(node.right))
        return result

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.data)
            result.extend(self._inorder_recursive(node.right))
        return result
    
    def postorder_traversal(self):
        return self._postorder_recursive(self.root)
    
    def _postorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._postorder_recursive(node.left))
            result.extend(self._postorder_recursive(node.right))
            result.append(node.data)
        return result
    
    def search(self, value, track = False):
        node = self.root
        if track:
            return self._search_recursion(value, node, 'root')
        else:
            return self._search_recursion(value, node)

    def _search_recursion(self, value, node, path=None):
        if value == node.data:
            return ('Found', path)
        elif value < node.data:
            return self._search_recursion(value, node.left, f'{path}.left' if path else None)
        elif value > node.data:
            return self._search_recursion(value, node.right, f"{path}.right" if path else None)
        
if __name__ == "__main__":
    # Binary Tree Test
    myTree = BinaryTree()
    myTree.insert(10)
    myTree.insert(5)
    myTree.insert(15)
    myTree.insert(3)
    myTree.insert(7)
    myTree.insert(12)
    myTree.insert(18)

    print("Preorder Traversal:", myTree.preorder_traversal())
    print("Inorder Traversal:", myTree.inorder_traversal())
    print("Postorder Traversal:", myTree.postorder_traversal())

    print(myTree.search(7, track=True))
