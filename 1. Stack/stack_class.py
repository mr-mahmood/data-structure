
class Stack:
    def __init__(self):
        self.top: int = 0
        self.stack: list = []
    
    def push(self, value):
        """Add an item to the top of the stack."""
        self.stack.append(value)
        self.top += 1
        
    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            temp = self.stack.pop(self.top-1)
            self.top -= 1
            return temp
        else:
            return 'stack is empty'
        
    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            temp = self.stack[self.top-1]
            return temp
        else:
            return 'stack is empty'

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == 0

    def size(self):
        """Return the size of the stack."""
        return self.top
    
    def show(self):
        """Note that this function is only for visualization and delete all values from stack to show its structure"""
        print_text = ''
        while True:
            if not self.is_empty():
                print_text = f'| {self.pop():^6} |\n----------\n' + print_text
            else:
                print_text = f'|        |\n----------\n' + print_text
                break
        return print_text
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(5)
    stack.push(-10)
    stack.push(3)
    stack.push(16)
    stack.push(7)
    
    print(f'stack size is: {stack.size()}')
    print(f'stack top iteam is: {stack.peek()}')
    print(f'pop item from stack: {stack.pop()}')
    print(f'stack size now after one pop is: {stack.size()}')
    print(f'stack top iteam now is: {stack.peek()}')
    print(f'stack is like bellow\n{stack.show()}')