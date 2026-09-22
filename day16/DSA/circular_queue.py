class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, val: int) -> bool:
        if self.is_full():
            return False
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def front(self) -> int | None:
        return None if self.is_empty() else self.queue[self.head]

    def rear(self) -> int | None:
        if self.is_empty():
            return None
        return self.queue[(self.tail - 1 + self.capacity) % self.capacity]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity


if __name__ == "__main__":
    cq = CircularQueue(3)
    print("Enqueue 10:", cq.enqueue(10))
    print("Enqueue 20:", cq.enqueue(20))
    print("Enqueue 30:", cq.enqueue(30))
    print("Enqueue 40 (Full):", cq.enqueue(40))
    print("Front:", cq.front())
    print("Rear:", cq.rear())
    print("Dequeue:", cq.dequeue())
    print("Enqueue 40:", cq.enqueue(40))
    print("Rear after wrap:", cq.rear())