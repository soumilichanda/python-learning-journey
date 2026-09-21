class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def find_middle(head: Node | None) -> Node | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def build_linked_list(arr: list[int]) -> Node | None:
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    odd_list = build_linked_list([1, 2, 3, 4, 5])
    mid_odd = find_middle(odd_list)
    print("Middle of [1, 2, 3, 4, 5]:", mid_odd.val if mid_odd else None)

    even_list = build_linked_list([1, 2, 3, 4, 5, 6])
    mid_even = find_middle(even_list)
    print("Middle of [1, 2, 3, 4, 5, 6]:", mid_even.val if mid_even else None)