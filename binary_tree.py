class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Node({self.value})"

# Building the tree
#         Document
#         /        \
# Official     College
# Documents    Documents
#   /   \           \
#  First Second    Photos

root = Node("Document")
root.left_child = Node("Official Documents")
root.right_child = Node("College Documents")

root.left_child.left_child = Node("First")
root.left_child.right_child = Node("Second")
root.right_child.right_child = Node("Photos")

# Just to test if tree is built correctly
print(root)                      # Node(Document)
print(root.left_child.value)     # Official Documents
print(root.left_child.left_child.value)  # First
