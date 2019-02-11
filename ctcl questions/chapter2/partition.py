from MyLinkedList import MyLinkedList

def partition(ll, x):
    if ll.head is None:
        return None
    current = ll.head
    buffer = []
    while current.next:
        if current.next.value < x:
            buffer.append(current.next.value)
            current.next = current.next.next
        else:
            current.next = current.next
    for num in buffer:
        ll.add_to_begining(num)

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.generate(10, 0, 10)
    print("Before :" + str(ll))
    partition(ll, 5)
    print("After :" + str(ll))

