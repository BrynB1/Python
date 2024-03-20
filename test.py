class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def processTree(root):
    stack = [root]
    output = []

    while len(stack) > 0:
        node = stack.pop()
        output.append(node.value)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return output

# Example usage:
# Create a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = Node(1, Node(2, Node(4), Node(5)), Node(3))

result = processTree(root)
print(result)
