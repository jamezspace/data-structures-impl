import java.util.ArrayList;

public class BplusTree {
    private static final int ORDER = 4;

    BPlusNode root;

    static class SplitResult {
        int promotedKey;
        BPlusNode rightNode;

        SplitResult(int promotedKey, BPlusNode rightNode) {
            this.promotedKey = promotedKey;
            this.rightNode = rightNode;
        }
    }

    static class BPlusNode {
        boolean isLeaf;
        ArrayList<Integer> keys;
        ArrayList<BPlusNode> children;
        BPlusNode next;

        BPlusNode(boolean isLeaf) {
            this.isLeaf = isLeaf;
            this.keys = new ArrayList<>();
            this.children = new ArrayList<>();
            this.next = null;
        }
    }

    BPlusNode createNode(boolean isLeaf) {
        return new BPlusNode(isLeaf);
    }

    void insert(int dataToInsert) {
        if (this.root == null) {
            this.root = this.createNode(true);
            this.root.keys.add(dataToInsert);
            return;
        }

        SplitResult splitNode = insertNode(this.root, dataToInsert);

        if (splitNode != null) {
            BPlusNode newRoot = this.createNode(false);
            newRoot.keys.add(splitNode.promotedKey);
            newRoot.children.add(this.root);
            newRoot.children.add(splitNode.rightNode);
            this.root = newRoot;
        }
    }

    SplitResult insertNode(BPlusNode root, int dataToInsert) {
        if (root.isLeaf) {
            insertKeyIntoLeaf(root, dataToInsert);

            if (root.keys.size() < ORDER) {
                return null;
            }

            return splitLeafNode(root);
        }

        int childIndex = findChildIndex(root, dataToInsert);
        SplitResult splitNode = insertNode(root.children.get(childIndex), dataToInsert);

        if (splitNode == null) {
            return null;
        }

        insertKeyIntoInternalNode(root, splitNode.promotedKey, splitNode.rightNode, childIndex);

        if (root.keys.size() < ORDER) {
            return null;
        }

        return splitInternalNode(root);
    }

    void insertKeyIntoLeaf(BPlusNode leafNode, int dataToInsert) {
        int insertIndex = 0;

        while (insertIndex < leafNode.keys.size() && leafNode.keys.get(insertIndex) < dataToInsert) {
            insertIndex++;
        }

        if (insertIndex >= leafNode.keys.size() || !leafNode.keys.get(insertIndex).equals(dataToInsert)) {
            leafNode.keys.add(insertIndex, dataToInsert);
        }
    }

    void insertKeyIntoInternalNode(BPlusNode node, int keyToInsert, BPlusNode childNode, int childIndex) {
        int insertIndex = 0;

        while (insertIndex < node.keys.size() && node.keys.get(insertIndex) < keyToInsert) {
            insertIndex++;
        }

        node.keys.add(insertIndex, keyToInsert);
        node.children.add(insertIndex + 1, childNode);
    }

    int findChildIndex(BPlusNode node, int dataToInsert) {
        int index = 0;

        while (index < node.keys.size() && dataToInsert >= node.keys.get(index)) {
            index++;
        }

        return index;
    }

    SplitResult splitLeafNode(BPlusNode leafNode) {
        BPlusNode newLeaf = this.createNode(true);

        int splitPoint = (leafNode.keys.size() + 1) / 2;

        while (leafNode.keys.size() > splitPoint) {
            newLeaf.keys.add(leafNode.keys.remove(splitPoint));
        }

        newLeaf.next = leafNode.next;
        leafNode.next = newLeaf;

        return new SplitResult(newLeaf.keys.get(0), newLeaf);
    }

    SplitResult splitInternalNode(BPlusNode internalNode) {
        BPlusNode newInternal = this.createNode(false);

        int middleIndex = internalNode.keys.size() / 2;
        int promotedKey = internalNode.keys.get(middleIndex);

        while (internalNode.keys.size() > middleIndex + 1) {
            newInternal.keys.add(internalNode.keys.remove(middleIndex + 1));
        }

        while (internalNode.children.size() > middleIndex + 1) {
            newInternal.children.add(internalNode.children.remove(middleIndex + 1));
        }

        internalNode.keys.remove(middleIndex);

        return new SplitResult(promotedKey, newInternal);
    }

    void traverseTreeInOrder(BPlusNode refNode) {
        if (refNode == null) {
            refNode = this.root;
        }

        if (refNode == null) {
            return;
        }

        BPlusNode currentNode = refNode;
        while (!currentNode.isLeaf) {
            currentNode = currentNode.children.get(0);
        }

        while (currentNode != null) {
            for (Integer key : currentNode.keys) {
                System.out.print(key + ", ");
            }
            currentNode = currentNode.next;
        }
    }

    void traverseTreePreOrder(BPlusNode refNode) {
        if (refNode == null) {
            refNode = this.root;
        }

        if (refNode == null) {
            return;
        }

        printNode(refNode);

        if (!refNode.isLeaf) {
            for (BPlusNode child : refNode.children) {
                traverseTreePreOrder(child);
            }
        }
    }

    void traverseTreePostOrder(BPlusNode refNode) {
        if (refNode == null) {
            refNode = this.root;
        }

        if (refNode == null) {
            return;
        }

        if (!refNode.isLeaf) {
            for (BPlusNode child : refNode.children) {
                traverseTreePostOrder(child);
            }
        }

        printNode(refNode);
    }

    void printNode(BPlusNode node) {
        System.out.print("[");
        for (int i = 0; i < node.keys.size(); i++) {
            System.out.print(node.keys.get(i));
            if (i < node.keys.size() - 1) {
                System.out.print(", ");
            }
        }
        System.out.print("], ");
    }

    boolean search(int dataToSearch) {
        BPlusNode currentNode = this.root;

        if (currentNode == null) {
            return false;
        }

        while (!currentNode.isLeaf) {
            int childIndex = findChildIndex(currentNode, dataToSearch);
            currentNode = currentNode.children.get(childIndex);
        }

        for (Integer key : currentNode.keys) {
            if (key == dataToSearch) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        BplusTree tree = new BplusTree();

        int[] values = { 10, 20, 5, 6, 12, 30, 7, 17 };
        for (int value : values) {
            tree.insert(value);
        }

        System.out.print("Inorder Traversal of the B+ Tree is: ");
        tree.traverseTreeInOrder(tree.root);
        System.out.println();

        System.out.print("Preorder Traversal of the B+ Tree is: ");
        tree.traverseTreePreOrder(tree.root);
        System.out.println();

        System.out.print("Postorder Traversal of the B+ Tree is: ");
        tree.traverseTreePostOrder(tree.root);
        System.out.println();

        int searchValue = 12;
        System.out.println("Search " + searchValue + ": " + tree.search(searchValue));
    }
}
