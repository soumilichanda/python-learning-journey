class QueueViaStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _shift_stacks(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int | None:
        self._shift_stacks()
        return self.out_stack.pop() if self.out_stack else None

    def peek(self) -> int | None:
        self._shift_stacks()
        return self.out_stack[-1] if self.out_stack else None

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = QueueViaStacks()
    for val in [1, 2, 3]:
        q.push(val)
    print("Peek:", q.peek())  # 1
    print("Pop:", q.pop())    # 1
    print("Pop:", q.pop())    # 2
    q.push(4)
    print("Peek:", q.peek())  # 3
    print("Empty:", q.empty())  # False