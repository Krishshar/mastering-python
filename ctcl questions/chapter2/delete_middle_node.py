from MyLinkedList import MyLinkedList
from random import choice

def delete_middle_node(ll):
    length = len(ll)
    if length < 3:
        return
    n = choice(range(1, length - 1))
    current = ll.head
    while n > 1:
        n -= 1
        current = current.next
    current.next = current.next.next

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.generate(10, 20, 40)
    print("Before: " + str(ll))
    delete_middle_node(ll)
    print("After: " + str(ll))