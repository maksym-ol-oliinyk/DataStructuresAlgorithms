from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.size() == 0

def main():
    stack = Stack()
    stack.push("elem 1")
    stack.push("elem 2")
    stack.push("elem 3")

    print(stack.container)
    print(stack.pop())
    print(stack.container)
    print(stack.peek())
    print(stack.container)

    print(stack.isEmpty())
    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())

if __name__ == "__main__":
    main()

