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

    def search(self, val: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def get_length(self) -> int:
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


if __name__ == "__main__":
    sll = SinglyLinkedList()
    for v in [15, 25, 35, 45]:
        sll.append(v)

    print("Length of list:", sll.get_length())
    print("Search 25:", sll.search(25))
    print("Search 99:", sll.search(99))