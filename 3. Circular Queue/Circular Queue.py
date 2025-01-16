class CircularQueue:
    def __init__(self, n):
        self.queue = [None] * n  # Fixed-size queue
        self.length = n          # Maximum size
        self.front = -1          # Front pointer
        self.rear = -1           # Rear pointer
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1
    
    def is_full(self):
        """Check if the queue is full."""
        return (self.rear + 1) % self.length == self.front
    
    def enqueue(self, value):
        """Add an item to the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.length
        self.queue[self.rear] = value
    
    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        if self.front == self.rear:  # Queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.length
        return value
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def size(self):
        """Return the current size of the queue."""
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.length - self.front + self.rear + 1
    
    def show(self):
        """Visualize the queue."""
        if self.is_empty():
            return "Queue is empty"
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.length
        return " -> ".join(map(str, result))


if __name__ == '__main__':
    queue = CircularQueue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print(f"Queue: {queue.show()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue.show()}")
    queue.enqueue(50)
    queue.enqueue(-10)
    queue.enqueue(-30)
    print(f"Queue: {queue.show()}")
    print(f"Front item: {queue.peek()}")
    print(f"Queue size: {queue.size()}")
