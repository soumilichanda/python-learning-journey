from binary_tree_traversals import TreeNode


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Tree: 3 -> Left: 9, Right: 20 (Left: 15, Right: 7)
    sample_tree = TreeNode(3)
    sample_tree.left = TreeNode(9)
    sample_tree.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(f"Maximum depth of tree: {max_depth(sample_tree)}")