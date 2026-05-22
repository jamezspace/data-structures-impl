import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

public class AvlTree {
    Node root;

    String[] imbalanceTypes = { "LL", "RR", "RL", "LR" };

    Node createNode(int data) {
        return new Node(data);
    }

    int calcHeightForLeftSubtree(Node refNode) {
        if (refNode == null || refNode.leftNode == null) {
            return 0;
        }

        return 1 + Math.max(
                calcHeightForLeftSubtree(refNode.leftNode),
                calcHeightForRightSubtree(refNode.leftNode));
    }

    int calcHeightForRightSubtree(Node refNode) {
        if (refNode == null || refNode.rightNode == null) {
            return 0;
        }

        return 1 + Math.max(
                calcHeightForLeftSubtree(refNode.rightNode),
                calcHeightForRightSubtree(refNode.rightNode));
    }

    int getBalanceFactor(Node refNode) {
        if (refNode == null) {
            return 0;
        }

        int lHeight = calcHeightForLeftSubtree(refNode);
        int rHeight = calcHeightForRightSubtree(refNode);

        return lHeight - rHeight;
    }

    boolean isRotationRequiredAroundNode(Node refNode) {
        int balanceFactor = getBalanceFactor(refNode);

        if (balanceFactor <= 1 && balanceFactor >= -1) {
            return true;
        }

        return false;
    }

    Node performLeftRotation(Node refNode) {
        if (refNode == null || refNode.rightNode == null) {
            return refNode;
        }

        Node newRoot = refNode.rightNode;
        Node transferNode = newRoot.leftNode;

        newRoot.leftNode = refNode;
        refNode.rightNode = transferNode;

        return newRoot;
    }

    Node performRightRotation(Node refNode) {
        if (refNode == null || refNode.leftNode == null) {
            return refNode;
        }

        Node newRoot = refNode.leftNode;
        Node transferNode = newRoot.rightNode;

        newRoot.rightNode = refNode;
        refNode.leftNode = transferNode;

        return newRoot;
    }

    Node rebalance(Node refNode, int insertedData) {
        if (refNode == null) {
            return null;
        }

        int balanceFactor = getBalanceFactor(refNode);

        // Left Left case
        if (balanceFactor > 1 && refNode.leftNode != null && insertedData < refNode.leftNode.data) {
            return performRightRotation(refNode);
        }

        // Right Right case
        if (balanceFactor < -1 && refNode.rightNode != null && insertedData > refNode.rightNode.data) {
            return performLeftRotation(refNode);
        }

        // Left Right case
        if (balanceFactor > 1 && refNode.leftNode != null && insertedData > refNode.leftNode.data) {
            refNode.leftNode = performLeftRotation(refNode.leftNode);
            return performRightRotation(refNode);
        }

        // Right Left case
        if (balanceFactor < -1 && refNode.rightNode != null && insertedData < refNode.rightNode.data) {
            refNode.rightNode = performRightRotation(refNode.rightNode);
            return performLeftRotation(refNode);
        }

        return refNode;
    }

    Node insertNode(Node refNode, int data) {
        if (refNode == null) {
            return createNode(data);
        }

        if (data < refNode.data) {
            refNode.leftNode = insertNode(refNode.leftNode, data);
        } else if (data > refNode.data) {
            refNode.rightNode = insertNode(refNode.rightNode, data);
        } else {
            return refNode;
        }

        return rebalance(refNode, data);
    }

    void insert(int data) {
        this.root = insertNode(this.root, data);
    }

    void traverseTreeInOrder(Node refNode) {
        if (refNode == null) {
            return;
        }

        if (refNode.leftNode != null) {
            this.traverseTreeInOrder(refNode.leftNode);
        }

        System.out.print(refNode.data + ", ");

        if (refNode.rightNode != null) {
            this.traverseTreeInOrder(refNode.rightNode);
        }
    }

    void traverseTreePostOrder(Node refNode) {
        if (refNode == null) {
            return;
        }

        if (refNode.leftNode != null) {
            this.traverseTreePostOrder(refNode.leftNode);
        }

        if (refNode.rightNode != null) {
            this.traverseTreePostOrder(refNode.rightNode);
        }

        System.out.print(refNode.data + ", ");
    }

    void traverseTreePreOrder(Node refNode) {
        if (refNode == null) {
            return;
        }

        System.out.print(refNode.data + ", ");

        if (refNode.leftNode != null) {
            this.traverseTreePreOrder(refNode.leftNode);
        }

        if (refNode.rightNode != null) {
            this.traverseTreePreOrder(refNode.rightNode);
        }
    }

    Map<String, Integer> getAllNodeDataLeftSide(Scanner input, int previousNodeData) {
        Map<String, Integer> children = new HashMap<>();

        System.out.format("Left Node of node %s: ", previousNodeData);
        int leftNodeData = input.nextInt();

        if (leftNodeData == 0) {
            children.put("left", null);
        } else {
            children.put("left", leftNodeData);
        }

        System.out.format("Right Node of node %s: ", previousNodeData);
        int rightNodeData = input.nextInt();

        if (rightNodeData == 0) {
            children.put("right", null);
        } else {
            children.put("right", rightNodeData);
        }

        return children;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        AvlTree tree = new AvlTree();

        System.out.print("What is the height of the tree: ");
        int treeHeight = input.nextInt();

        // array list to hold the entered avl tree data
        ArrayList<String> avlTree = new ArrayList<>();

        // Note: 0 represents a null node, hence '0' is not permitted as an input in the tree
        System.out.print("Root node: ");
        int rootNodeData = input.nextInt();
        tree.root = tree.createNode(rootNodeData);

        Queue<Node> nodeQueue = new LinkedList<>();
        nodeQueue.add(tree.root);

        int currentLevel = 0;
        while (!nodeQueue.isEmpty() && currentLevel < treeHeight) {
            int nodesAtThisLevel = nodeQueue.size();

            for (int i = 0; i < nodesAtThisLevel; i++) {
                Node currentNode = nodeQueue.remove();
                Map<String, Integer> children = tree.getAllNodeDataLeftSide(input, currentNode.data);
                avlTree.add(currentNode.data + ": " + children);

                Integer leftChild = children.get("left");
                Integer rightChild = children.get("right");

                if (leftChild != null) {
                    currentNode.leftNode = tree.createNode(leftChild);
                    nodeQueue.add(currentNode.leftNode);
                }

                if (rightChild != null) {
                    currentNode.rightNode = tree.createNode(rightChild);
                    nodeQueue.add(currentNode.rightNode);
                }
            }

            currentLevel++;
        }

        System.out.println("Avl Tree: " + avlTree);
    }
}
