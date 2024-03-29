from random import randint

class LinkedListNode:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self

    # def print_reverse(self):
    # 	if self.head is None:
    # 		return
    # 	self.print_reverse(self.head.next)
    # 	print(self.head.value)

    def reverse(self):
        current = self.head
        prev = None
        nxt = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList([1, 2, 4, 5, 6])
    print(ll)
    ll.reverse()
    print(ll)