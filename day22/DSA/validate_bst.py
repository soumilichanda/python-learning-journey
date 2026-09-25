class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, low: float, high: float) -> bool:
        if not node:
            return True

        # Node value must be strictly within (low, high)
        if not (low < node.val < high):
            return False

        # Recurse left with updated ceiling, and right with updated floor
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    # Valid BST:
    #      2
    #     / \
    #    1   3
    valid_tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Valid tree check: {is_valid_bst(valid_tree)} (Expected: True)")

    # Invalid BST:
    #      5
    #     / \
    #    1   4
    #       / \
    #      3   6
    invalid_tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Invalid tree check: {is_valid_bst(invalid_tree)} (Expected: False)")