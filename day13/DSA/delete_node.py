class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, val: int) -> bool:
        if not self.head:
            return False

        if self.head.val == val:
            self.head = self.head.next
            return True

        curr = self.head
        while curr.next and curr.next.val != val:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
            return True

        return False

    def to_list(self) -> list[int]:
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements


if __name__ == "__main__":
    sll = SinglyLinkedList()
    for v in [10, 20, 30, 40]:
        sll.append(v)
    print("Initial:", sll.to_list())

    sll.delete_by_value(10)  # Delete head
    print("After deleting 10:", sll.to_list())

    sll.delete_by_value(30)  # Delete middle
    print("After deleting 30:", sll.to_list())

    sll.delete_by_value(40)  # Delete tail
    print("After deleting 40:", sll.to_list())