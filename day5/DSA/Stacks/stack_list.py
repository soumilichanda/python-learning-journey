# 9. Stack using Python list (LIFO)
class ListStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Current Stack:", self.stack)

if __name__ == "__main__":
    stack = ListStack()
    print("=== Interactive Stack Demo ===")
    
    count = int(input("How many items do you want to push into the stack? "))
    for i in range(count):
        val = input(f"Enter item {i + 1}: ")
        stack.push(val)

    stack.display()
    
    pop_choice = input("Do you want to pop an item? (y/n): ").strip().lower()
    if pop_choice == 'y':
        print("Popped item:", stack.pop())
        stack.display()
        