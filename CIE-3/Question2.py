class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data 
        self.left = None  
        self.right = None  


class BinaryTree:
    """Class to represent a binary tree."""
    def __init__(self):
        self.root = None  

    def insert(self, data):
        """Insert a new node into the binary tree."""
        if self.root is None:
            self.root = TreeNode(data) 
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Helper method to insert a node recursively."""
        if data < node.data:
            
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
           
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def in_order_traversal(self):
        """Perform in-order traversal of the binary tree."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        """Helper method to perform in-order traversal recursively."""
        if node is not None:
            self._in_order_recursive(node.left, result)  
            result.append(node.data) 
            self._in_order_recursive(node.right, result)  


# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("In-order traversal:", tree.in_order_traversal())


Output:
/usr/bin/python3 /home/rvu/question2.py
In-order traversal: [20, 30, 40, 50, 60, 70, 80]
