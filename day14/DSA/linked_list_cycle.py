class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def has_cycle(head: Node | None) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    # Create list: 3 -> 2 -> 0 -> -4 -> points back to node 2
    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # Cycle created

    print("Has cycle (cyclic list):", has_cycle(n1))

    # Acyclic test: 1 -> 2 -> 3
    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a1.next = a2
    a2.next = a3

    print("Has cycle (acyclic list):", has_cycle(a1))