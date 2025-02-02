class Node:
    """
    A class representing a node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value  # The data stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class LinkList:
    """
    A class representing a doubly linked list.
    """
    def __init__(self):
        self.head = None  # The first node in the linked list
    
    def __len__(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def __getitem__(self, index):
        
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        count = 0
        temp = self.head
        while temp:
            if count == index:
                return temp.value
            else:
                temp = temp.next
                count += 1
    
    def __setitem__(self, index, value):
        
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        count = 0
        temp = self.head
        while temp:
            if count == index:
                temp.value = value
                return
            else:
                temp = temp.next
                count += 1
      
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self):
            result = self[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.
        """
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        return " <-> ".join(result) if result else "Empty List"

    def __repr__(self):
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return f"LinkList([{', '.join(values)}])"
    
    def append(self, value) -> None:
        """
        Adds a new node with the given value to the end of the linked list.
        
        Args:
            value (any): The value to be stored in the new node.
        """
        new_node = Node(value)
        
        if not self.head:  # If the list is empty, set head to the new node
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node  # Link last node to new node
            new_node.prev = temp  # Link new node back to last node
    
    def insert(self, index: int, value) -> None:
        """
        Inserts a new node with the given value at the specified index.
        
        Args:
            index (int): The position to insert the new node.
            value (any): The value to be stored in the new node.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        
        new_node = Node(value)
        
        if index == 0:  # Insert at the beginning
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
    
    def extend(self, other_head: Node) -> None:
        """
        Extends the current linked list by appending another linked list.
        
        Args:
            other_head (Node): The head node of the linked list to append.
        """
        if not self.head:
            self.head = other_head
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        while other_head:
            temp.next = other_head
            other_head.prev = temp
            temp = temp.next
            other_head = other_head.next
    
    def remove(self, value) -> None:
        """
        Removes the first occurrence of a node containing the given value.
        
        Args:
            value (any): The value to remove from the linked list.
        
        Raises:
            ValueError: If the value is not found in the linked list.
        """
        temp = self.head
        while temp:
            if temp.value == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        raise ValueError(f"Value {value} not found in list")


if __name__ == '__main__':
    temp_list = LinkList()
    temp_list.append(1)
    temp_list.append(2)
    
    t = LinkList()
    t.append(0)
    t.insert(0, -1)
    t.extend(temp_list.head)
    
    print("Length:", len(t))
    print("List:", t)

    print(t[3])
    t[3] = 10
    print(t[3])
    
    print(repr(t))
    
    for i in t:
        print(i)
        