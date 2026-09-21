class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def reverse_linked_list(head: Node | None) -> Node | None:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def build_linked_list(arr: list[int]) -> Node | None:
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


def to_list(head: Node | None) -> list[int]:
    elements = []
    curr = head
    while curr:
        elements.append(curr.val)
        curr = curr.next
    return elements


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print("Original:", to_list(head))
    reversed_head = reverse_linked_list(head)
    print("Reversed:", to_list(reversed_head))
    