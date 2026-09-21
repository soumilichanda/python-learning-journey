class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def to_list(self) -> list[int]:
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_tail(10)
    sll.insert_at_tail(20)
    sll.insert_at_tail(30)
    sll.insert_at_head(5)
    print("Linked List items:", sll.to_list())