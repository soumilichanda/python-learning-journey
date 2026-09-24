class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode | None) -> list[int]:
    result: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return
        result.append(node.val)  # Visit Root
        dfs(node.left)           # Recurse Left
        dfs(node.right)          # Recurse Right

    dfs(root)
    return result


def inorder_traversal(root: TreeNode | None) -> list[int]:
    result: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return
        dfs(node.left)           # Recurse Left
        result.append(node.val)  # Visit Root
        dfs(node.right)          # Recurse Right

    dfs(root)
    return result


def postorder_traversal(root: TreeNode | None) -> list[int]:
    result: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return
        dfs(node.left)           # Recurse Left
        dfs(node.right)          # Recurse Right
        result.append(node.val)  # Visit Root

    dfs(root)
    return result


if __name__ == "__main__":
    # Constructing Tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    tree_root.right = TreeNode(3)

    print("=== Binary Tree Depth-First Search Traversals ===")
    print(f"Pre-order  (Root, Left, Right): {preorder_traversal(tree_root)}")
    print(f"In-order   (Left, Root, Right): {inorder_traversal(tree_root)}")
    print(f"Post-order (Left, Right, Root): {postorder_traversal(tree_root)}")