from MyLinkedList import MyLinkedList

def sum_lists(ll1, ll2):
    return int(''.join(str(ll1)[::-1].split(' >-- '))) + int(''.join(str(ll2)[::-1].split(' >-- ')))

if __name__ == "__main__":
    ll1 = MyLinkedList()
    ll1.generate(3, 0, 9)
    ll2 = MyLinkedList()
    ll2.generate(3, 0, 9)
    print(f"Sum of {ll1} & {ll2} is {sum_lists(ll1, ll2)}") 