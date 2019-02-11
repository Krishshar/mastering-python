from random import randint

class MyLinkedListNode:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
    
    def __str__(self):
        return str(self.value)

class MyLinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __str__(self):
        values = [str(x) for x in self]
        return ' --> '.join(values)

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def add(self, value):
        if self.head is None:
            self.tail = self.head = MyLinkedListNode(value)
        else:
            self.tail.next = MyLinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_to_begining(self, value):
        if self.head is None:
            self.tail = self.head = MyLinkedListNode(value)
        else:
            self.head = MyLinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for val in values:
            self.add(val)
        return self
    
    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self

    def print_reverse(self):
        if self.head is None:
            return 
        self.print_reverse(self.head.next)
        print(self.head.value)