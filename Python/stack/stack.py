class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, value):
        """Push an element onto the stack."""
        self.stack.append(value)
        print(f"{value} pushed onto the stack.")

    def pop(self):
        """Pop an element from the stack."""
        if self.is_empty():
            print("Stack underflow! Cannot pop.")
            return None  # Sentinel value for underflow
        return self.stack.pop()

    def peek(self):
        """Peek at the top element of the stack."""
        if self.is_empty():
            print("Stack is empty! Cannot peek.")
            return None  # Sentinel value for empty stack
        return self.stack[-1]

    def display(self):
        """Display the current stack."""
        print("Stack:", self.stack)


# Main function to demonstrate stack operations
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display the stack
    stack.display()

    # Peek the top element
    print(f"Top element: {stack.peek()}")

    # Pop elements from the stack
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")

    # Peek after popping
    print(f"Top element: {stack.peek()}")

    # Pop remaining elements
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")  # Should show underflow
