'''Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    """Encodes a tree to a single string.
    """
    def helper(node):
        if node:
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)
        else:
            vals.append('#')

    vals = []
    helper(root)
    return ' '.join(vals)

def deserialize(data):
    """Decodes your encoded data to tree.
    """
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node

    vals = iter(data.split())
    return helper()
def main():
    # Create a binary tree for testing
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Serialize the tree
    serialized_tree = serialize(root)
    print(f"Serialized tree: {serialized_tree}")

    # Deserialize the tree
    deserialized_root = deserialize(serialized_tree)
    print(f"Deserialized tree: {deserialized_root.val}, {deserialized_root.left.val}, {deserialized_root.right.val}")

if __name__ == "__main__":
    main()
