class Simple_Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        if isinstance(value, list):
            self.queue.extend(value)
        else:
            self.queue.append(value)
        return self
        
    def dequeue(self):
        if not self.queue:
            return print("Queue is Empty")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) <= 0
        
    def print_queue(self):
        return print(f"Queue: {self.queue}")
    