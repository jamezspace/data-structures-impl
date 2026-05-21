from binarytrees import Node
class AVL:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)

        balance_factor = self.get_balance(node)

        # Left Left Case
        if balance_factor > 1 and data < node.left.data:
            return self.right_rotate(node)

        # Right Right Case
        if balance_factor < -1 and data > node.right.data:
            return self.left_rotate(node)

        # Left Right Case
        if balance_factor > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance_factor < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        return y

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.data)
            result.extend(self._inorder_recursive(node.right))
        return result

if __name__ == "__main__":
    # AVL Tree Test
    avlTree = AVL()
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avlTree.insert(val)
    
    print("Inorder Traversal of the AVL Tree is:", avlTree.inorder_traversal())

