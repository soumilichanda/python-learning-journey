from collections import deque

def run_simulator():
    stack = []
    queue = deque()

    while True:
        print("\n--- Stack & Queue Simulator ---")
        print("1. Push (Stack)")
        print("2. Pop (Stack)")
        print("3. Display Stack")
        print("4. Enqueue (Queue)")
        print("5. Dequeue (Queue)")
        print("6. Display Queue")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            val = input("Enter value to push: ")
            stack.append(val)
            print(f"Pushed '{val}' to Stack.")
        elif choice == '2':
            print("Popped:", stack.pop() if stack else "Stack is empty!")
        elif choice == '3':
            print("Current Stack (Bottom -> Top):", stack)
        elif choice == '4':
            val = input("Enter value to enqueue: ")
            queue.append(val)
            print(f"Enqueued '{val}' to Queue.")
        elif choice == '5':
            print("Dequeued:", queue.popleft() if queue else "Queue is empty!")
        elif choice == '6':
            print("Current Queue (Front -> Rear):", list(queue))
        elif choice == '7':
            print("Exiting simulator.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run_simulator()