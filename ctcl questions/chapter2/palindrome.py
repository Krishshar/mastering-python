from MyLinkedList import MyLinkedList

def palindrome(ll):
    if ll.head is None:
        return None
    if len(ll) == 1:
        return True
    

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.generate(10, 10, 99)
    print(ll)
    print(palindrome(ll))