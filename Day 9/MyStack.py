class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue = [x]
        while len(self.stack) > 0:
            self.queue.append(self.stack.pop())
        while len(self.queue) > 0:
            self.stack.append(self.queue.pop())
        return self.stack

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.stack) == 0 else False