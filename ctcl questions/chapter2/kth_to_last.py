# Write a algorith that returns kth_to_last element of a linked list
from MyLinkedList import MyLinkedList

def kth_to_last(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if runner is None:
            return None
        runner = runner.next
    
    while runner:
        current = current.next
        runner = runner.next
    
    return current

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.generate(10, 100, 199)
    print(ll)
    print(kth_to_last(ll, 6))