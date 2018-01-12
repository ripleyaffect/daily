"""
A unival tree (which stands for "universal value") is a tree where all nodes
have the same value.

Given the root to a binary tree, count the number of unival subtrees.

"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        """Create a new tree node

        :param value: value to store in the node
        :param left: left TreeNode. Default `None`
        :param right: right TreeNode. Default `None`

        """
        self.value = value
        self.left = left
        self.right = right


def unival_tree_count(node, root=True):
    """Return the number of unival subtrees in the tree with root `node`
    if at root, else a `tuple` with the unival count and the number of trees
    represented

    A tree with no children is always a unival tree
    A tree with children is a unival tree if:
        - Its value is the same as its children's values
        - Its children are unival trees

    we check if the children are unival trees by comparing their unival count
    to the number of trees represetned. If they are they same, then the child
    is a unival tree

    :param node: `TreeNode` to use as the root of the tree
    :param root: `bool` of whether this node is the root (default True)

    """
    # Handle base case
    if node is None:
        return 0 if root else (0, 0)

    # Count the left subtree's unival trees
    left_count, left_subtrees = unival_tree_count(node.left, False)
    left_unival = (
        node.value == node.left.value) and (left_count == left_subtrees
    ) if node.left else True

    # Count the right subtree's unival trees
    right_count, right_subtrees = unival_tree_count(node.right, False)
    right_unival = (
        node.value == node.right.value) and (right_count == right_subtrees
    ) if node.right else True

    # Find the current count
    count = left_count + right_count + int(left_unival and right_unival)

    # Return either the value (at root) or the count & unival subtree count + 1
    return count if root else (count, left_subtrees + right_subtrees + 1)


if __name__ == '__main__':
    # Set up the tree
    left_left = TreeNode(5)
    left_right = TreeNode(5)
    right_right = TreeNode(5)
    left = TreeNode(4, left_left, left_right)
    right = TreeNode(5, None, right_right)
    root = TreeNode(5, left, right)

    print(unival_tree_count(root))
