"""
Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.
"""

import json


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

    def __repr__(self):
        """Return a string representation of `self`"""
        return '\nValue: {}\nLeft: [{}]\nRight: [{}]'.format(
            self.value, self.left, self.right)


def get_left_index(index):
    """Return index of this index's left child

    :param index: `int` index of the node to get left child's index for

    """
    return index * 2


def get_right_index(index):
    """Return index of this index's right child

    :param index: `int` index of the node to get right child's index for

    """
    return index * 2 + 1


def serialize(node, index=1, tree_dict=None):
    """Return a serialized tree

    We serialize a tree by keying a node's value by its index in the "array
    representaion" the tree, then recursively adding its children at their
    indices, if they exist.

    After all nodes have been added to the `tree_dict`, the result is
    serialized as JSON to get a string representation and returned.

    :param node: `TreeNode` to add to the `tree_dict`
    :param index: `int` index of node, used to create key and calculate
        indices of children. Defaults to 1 (the root)
    :param tree_dict: `dict` of tree, passed to child serializer function calls

    """
    # Short-circuit if no node to add to the tree
    if node is None:
        return

    # Create the `tree_dict` if needed
    tree_dict = tree_dict or {}

    # Add the node value to the `tree_dict`
    tree_dict[index] = node.value

    # Add the node's children to the tree
    serialize(node.left, get_left_index(index), tree_dict)
    serialize(node.right, get_right_index(index), tree_dict)

    # Serialize if at the root
    return json.dumps(tree_dict) if index == 1 else tree_dict


def deserialize(tree, index=1):
    """Return a deserialized tree

    We ingest a serialized version of the tree `dict` representaion,
    deserialize it, then recurseivly create its sub-trees, turning them back
    into nodes.

    :param tree: `str` or `dict` representation of the tree
    :param index: `int` index of the node being deserialized.
        Defaults to 1 (the root)

    """
    # Deserialize the tree if needed
    if type(tree) == str:
        tree = json.loads(tree)

    # Get this node's value
    value = tree.get(str(index))

    # Return `None` if no node is present
    if value is None:
        return None

    # Calculate the indices for this node's children
    left_index = get_left_index(index)
    right_index = get_right_index(index)

    # Create children recursively
    left_node = deserialize(tree, left_index)
    right_node = deserialize(tree, right_index)

    # Return a new node
    return TreeNode(value, left_node, right_node)


if __name__ == '__main__':
    # Bulid the test tree
    left_left = TreeNode('four')
    left_right = TreeNode('five')
    right_left = TreeNode('six')
    right_right = TreeNode('seven')
    left = TreeNode('two', left_left, left_right)
    right = TreeNode('three', right_left, right_right)
    root = TreeNode('one', left, right)

    # Serialize the tree
    serialized_tree = serialize(root)

    # Print the serialized and re-serialized tree, to show deserializing works
    print(serialized_tree)
    print(serialize(deserialize(serialized_tree)))
    print(deserialize(serialized_tree))
