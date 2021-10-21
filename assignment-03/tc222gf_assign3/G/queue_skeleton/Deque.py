from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, Node)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.nxt = self.head
            self.head = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        if self.head is None:
            return "{"+" "+"}"
        else:
            s = "{ "
            node = self.head
            while node.value is not None:
                s += str(node.value)+" "
                node = node.nxt
                if node is None:
                    break
            s += "}"
            return s

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, Node)
        if self.head is None:
            self.head = new
            self.tail = new
            new.nxt = None
        else:
            self.tail.nxt = new
            self.tail = new
            new.nxt = None
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.size == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return removed.value
        else:
            removed = self.head
            self.head = self.head.nxt
            self.size -= 1
            return removed.value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling

    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.size == 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return removed.value
        else:
            removed = self.tail
            before = self.head
            for i in range(self.size-2):
                before = before.nxt
            before.nxt = None
            self.tail = before
            self.size -= 1
            return removed.value
