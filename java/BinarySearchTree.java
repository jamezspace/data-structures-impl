class BinarySearchTree {
    Node root;

    Node createNode(int data) {
        return new Node(data);
    }

    void insert(int dataToInsert) {       
        // when there is no existing root
        if (this.root == null) {
            this.root = this.createNode(dataToInsert);
        } else 
            insertNode(this.root, dataToInsert);
    }

    void insertNode(Node root, int dataToInsert) {
        if (root.data > dataToInsert) {
            if(root.leftNode == null) 
                root.leftNode = this.createNode(dataToInsert);
            else insertNode(root.leftNode, dataToInsert);
        } else {
            if(root.rightNode == null) 
                root.rightNode = this.createNode(dataToInsert);
            else insertNode(root.rightNode, dataToInsert);
        }
    }

    void traverseTreeInOrder(Node refNode) {
        if (refNode == null) refNode = this.root;

        if (refNode.leftNode != null) {
            this.traverseTreeInOrder(refNode.leftNode);
        }

        System.out.print(refNode.data + ", ");

        if (refNode.rightNode != null) {
            this.traverseTreeInOrder(refNode.rightNode);
        }
    }

    void traverseTreePostOrder(Node refNode) {
        if (refNode == null) refNode = this.root;

        if (refNode.leftNode != null) {
            this.traverseTreePostOrder(refNode.leftNode);
        }

        if (refNode.rightNode != null) {
            this.traverseTreePostOrder(refNode.rightNode);
        }

        System.out.print(refNode.data + ", ");
    }

    void traverseTreePreOrder(Node refNode) {
        if (refNode == null) refNode = this.root;

        System.out.print(refNode.data + ", ");

        if (refNode.leftNode != null) {
            this.traverseTreePreOrder(refNode.leftNode);
        }

        if (refNode.rightNode != null) {
            this.traverseTreePreOrder(refNode.rightNode);
        }
    }
}