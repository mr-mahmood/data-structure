class Queue:
    def __init__(self):
        self.queue: list = []
    
    def insert(self, value):
        """Add an item to the top of the queue."""
        self.queue.append(value)
        
    def dequeue(self):
        """Remove and return the top item of the queue."""
        if not self.is_empty():
            temp = self.queue.pop(0)
            return temp
        else:
            return 'queue is empty'
        
    def peek(self):
        """Return the top item of the queue without removing it."""
        if not self.is_empty():
            temp = self.queue[0]
            return temp
        else:
            return 'queue is empty'

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)
    
    def show(self):
        """Note that this function is only for visualization and delete all values from  queue to show its structure"""
        print_text = ''
        while True:
            if not self.is_empty():
                print_text = f'| {self.queue.pop(0):^6} |\n----------\n' + print_text
            else:
                print_text = f'|        |\n----------\n' + print_text
                break
        return print_text

if __name__ == '__main__':
    queue = Queue()
    queue.insert(10)
    queue.insert(5)
    queue.insert(-10)
    queue.insert(3)
    queue.insert(16)
    queue.insert(7)
    
    print(f'queue size is: {queue.size()}')
    print(f'queue first iteam is: {queue.peek()}')
    print(f'pop item from queue: {queue.dequeue()}')
    print(f'queue size now after one pop is: {queue.size()}')
    print(f'queue top iteam now is: {queue.peek()}')
    print(f'queue is like bellow\n{queue.show()}')