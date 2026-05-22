class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, value):
        if self.isFull():
            print('Stack Overflow')
            return self
        self.stack.append(value)
        return self
    
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        
        return self.stack.pop()
    
    def isEmpty(self):
        return True if not self.stack else False
    
    def isFull(self):
        return True if len(self.stack) == self.size else False
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return False
