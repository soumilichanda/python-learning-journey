# 10. Queue using deque (FIFO)
from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Current Queue:", list(self.queue))

if __name__ == "__main__":
    queue = DequeQueue()
    print("=== Interactive Queue Demo ===")

    count = int(input("How many items do you want to enqueue? "))
    for i in range(count):
        val = input(f"Enter item {i + 1}: ")
        queue.enqueue(val)

    queue.display()

    deq_choice = input("Do you want to dequeue an item? (y/n): ").strip().lower()
    if deq_choice == 'y':
        print("Dequeued item:", queue.dequeue())
        queue.display()