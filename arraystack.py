# arraystack.py
# Nick Mock

from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation"""
    
    # Class variable
    DEFAULT_CAPACITY = 10
    
    # Constructor
    def __init__(self, SourceCollection = None):
        """Sets the initial state of self, which includes the contents of SourceCollection, if it's present."""
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, SourceCollection)
        
    
    # Accessor Methods
    def __iter__(self):
        """Supports iteration over a view of self. Visits items from bottom to top of stack"""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1
            
    def peek(self):
        """Returns the item at the top of the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        # Returns the item on the top of the stack
        return self.items[len(self) - 1]
    
    def clear(self):
        """Makes self become empty"""
        self.size = 0 
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        
    def push(self, item):
        """Inserts item at top of the stack"""
        # Resize array here if necessary
        if len(self) == len(self.items):
            temp = Array(2 * len(self))
            for i in range (len(self)):
                temp[i] = self.items[i]
            self.items = temp
        # Add the item and increase the sixe
        self.items[len(self)] = item
        self.size += 1
            
    def pop(self):
        """Removes and returns the item at the top of the stack, stack can't be empty"""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        
        # get the item and decrement the size
        oldItem = self.items[len(self) - 1]
        self.size -= 1
        
        # Resize the array here if necessary same as shrink
        if len(self) <= len(self.items) // 4 and \
           len(self.items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            temp = Array(len(self.items) // 2)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp
            
        # Return the popped item
        return oldItem
    
    