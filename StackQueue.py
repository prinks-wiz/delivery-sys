
from queue import Empty

class Stacks:
    """create a stack class(LIFO)"""
    def __init__(self):
        """create an empty stack"""
        self.data = []

    def __len__(self):
        """return the number of elements in the stack"""
        return len(self.data)

    def is_empty(self):
        """return true if the number of elements in the stack is zero"""
        return len(self.data) == 0

    def push(self, element):
        """adding an element to the stack"""
        self.data.append(element)

    def top(self):
        """return the top element of the stack"""
        """raise empty exception if the stack is empty"""
        if self.is_empty():
            return 'stack is empty'
        return self.data[-1]
        """returns the last element of the stack"""

    def pop(self):
        """remove and return the last element of the stack"""
        if self.is_empty():
            raise 'stack is empty'
        return self.data.pop()
        """returns and removes the last element from the stack if the stack is not empty"""



class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 20         # minimum capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    
  def enqueue(self, e):
    """Add an element to the back of queue."""
    if e in self._data:
        return
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned
  
  def display(self):
    print(self._data)
