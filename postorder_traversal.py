# Python3 program for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do postorder tree traversal
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val, end=" ")


# Driver code
if __name__ == "__main__":
    # Get input from user
    values = input("Enter values separated by space: ").split()

    # Create root node
    root = Node(int(values[0]))
    
    # Insert values into the tree
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(values):
            if values[i] != "None":
                node.left = Node(int(values[i]))
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] != "None":
                node.right = Node(int(values[i]))
                queue.append(node.right)
            i += 1

    # Print postorder traversal
    print("\nPostorder traversal of binary tree is:")
    printPostorder(root)
