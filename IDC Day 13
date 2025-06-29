# -implement a stack using pop, push and peek.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty! Nothing to pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty! Nothing to peek.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (top to bottom):", list(reversed(self.items)))


# Example usage
stack = Stack()
#stack.peek()
stack.push(10) #added 10 to our stack
stack.peek() #peek to see the top element on our stack
stack.push(20) #added 20 to our stack
stack.display() # Display our stack
stack.pop() #Pop the top element from our stack
stack.display() #Display our stack again after popping
