class Node:
    def __init__(self, data: int | list[int], left: Node =None, mid: Node =None, right: Node =None):
        self.left = left
        self.right = right
        self.mid = mid #represents all middle children of the node, if any 
        self.keys = [data] if type(data) != list else data
    
class BTree:
    def __init__(self, m, root= None):
        self.m = m
        self.root = root
    
    def insert(self, data:int):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node:Node, data):
        max_key = max(node.keys)
        min_key = min(node.keys)

        if data < min_key:
            if node.left is None: #leaf node
                node.keys.append(data)
                node.keys.sort()
                if self.root == node and len(node.keys) > 2:
                    self._balance_up(node)
            else:
                self._insert_recursive(node.left, data)
                self._balance_up(node)
        elif data > max_key:
            if node.right is None:
                node.keys.append(data)
                node.keys.sort()
                if self.root == node and len(node.keys) > 2:
                    self._balance_up(node)
            else:
                self._insert_recursive(node.right, data)
                self._balance_up(node)
        else:
            if node.mid is None:
                node.keys.append(data)
                node.keys.sort()
                if self.root == node and len(node.keys) > 2:
                    self._balance_up(node)
            else:
                self._insert_recursive(node.mid, data)
                self._balance_up(node)
    
    def _balance_up(self, node: Node):
        if self.root == node and len(node.keys) > 2:
            mid_val = node.keys.pop(1)

            new_root = Node(mid_val)
            l_node = Node(node.keys[:1], node.left, None, None)
            r_node = Node(node.keys[1:], None, None, node.right)
            new_root.left = l_node
            new_root.right = r_node
            self.root = new_root

            if node.mid != None:
                r_node = [x for x in node.mid.keys if x <= mid_val]
                l_node = [x for x in node.mid.keys if x > mid_val]
                node.mid = None
                self.root.left.right = Node(r_node)
                self.root.right.left = Node(l_node)

        elif len(node.left.keys) > self.m - 1:
            p_val = node.left.keys.pop(-2)
            node.keys.append(p_val)
            node.keys.sort()
            if node.mid == None:
                node.mid = Node(node.left.keys.pop(-1))
            else:
                node.mid.keys.append(node.left.keys.pop(-1))
                node.mid.keys.sort()
            
            if node.left.mid != None:
                r_node = [x for x in node.left.mid.keys if x <= p_val]
                l_node = [x for x in node.left.mid.keys if x > p_val]
                node.left.mid = None
                node.left.right = Node(r_node)
                node.mid.left = Node(l_node)
        elif len(node.right.keys) > self.m - 1:
            p_val = node.right.keys.pop(-2)
            node.keys.append(p_val)
            node.keys.sort()
            if node.mid == None:
                new_node = Node(node.right.keys[:-1])
                node.mid = new_node
            else:
                node.mid.keys.extend(node.right.keys[:-1])
                node.mid.keys.sort()
            node.right.keys = node.right.keys[-1:]

            if node.right.mid != None:
                r_node = [x for x in node.right.mid.keys if x <= p_val]
                l_node = [x for x in node.right.mid.keys if x > p_val]
                node.right.mid = None
                node.right.left = Node(l_node)
                node.mid.right = Node(r_node)
        elif node.mid is not None and len(node.mid.keys) > self.m - 1:
            p_val = node.mid.keys.pop(-2)
            node.keys.append(p_val)
            node.keys.sort()
    
    def search(self, data: int) -> bool:
        return self._search_recursive(self.root, data)
    def _search_recursive(self, node: Node, data: int) -> bool:
        if node is None:
            return False
        if data in node.keys:
            return True
        max_key = max(node.keys)
        min_key = min(node.keys)

        if data < min_key:
            return self._search_recursive(node.left, data)
        elif data > max_key:
            return self._search_recursive(node.right, data)
        else:
            return self._search_recursive(node.mid, data)
    
    def inorder_traversal(self) -> list[int]:
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node: Node, result: list[int]):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.extend(node.keys)
            self._inorder_recursive(node.mid, result)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":

    # BTree Test:
    b_tree = BTree(4)
    values = [10, 20, 40, 50, 60, 70, 80, 5, 15, 30, 108, 200, 77]
    for val in values:
        b_tree.insert(val)
        
    print(b_tree.inorder_traversal())
    print(b_tree.search(15))
    print(b_tree.root.keys) 
    print(b_tree.root.left.keys)
    print(b_tree.root.right.keys)


        