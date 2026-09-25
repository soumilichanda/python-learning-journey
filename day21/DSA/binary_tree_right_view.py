from collections import deque
from level_order_traversal import TreeNode


def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    right_view: list[int] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # The last element in the current level queue is visible from the right side
            if i == level_size - 1:
                right_view.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_view


if __name__ == "__main__":
    # Tree: 1 -> Left: 2 (Right: 5), Right: 3 (Right: 4)
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))

    print("=== Binary Tree Right Side View ===")
    print(right_side_view(root))  # [1, 3, 4]