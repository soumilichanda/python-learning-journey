class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, val: int) -> None:
        if not self.root:
            self.root = TreeNode(val)
            return

        curr = self.root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                # BSTs do not permit duplicate values
                break

    def search(self, target: int) -> bool:
        curr = self.root
        while curr:
            if target == curr.val:
                return True
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def find_min(self) -> int | None:
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def find_max(self) -> int | None:
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val


if __name__ == "__main__":
    bst = BinarySearchTree()
    for num in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(num)

    print("=== Binary Search Tree Operations ===")
    print(f"Search 40: {bst.search(40)} (Expected: True)")
    print(f"Search 99: {bst.search(99)} (Expected: False)")
    print(f"Minimum Value: {bst.find_min()} (Expected: 20)")
    print(f"Maximum Value: {bst.find_max()} (Expected: 80)")