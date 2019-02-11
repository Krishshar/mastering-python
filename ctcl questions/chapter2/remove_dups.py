from MyLinkedList import MyLinkedList

def remove_dups(ll):
	if ll.head is None:
		return

	current = ll.head
	seen = {current.value}
	while current.next:
		if current.next.value in seen:
			current.next = current.next.next
		else:
			seen.add(current.next.value)
			current = current.next
	return ll

def remove_dups_followup(ll):
	if ll.head is None:
		return
	
	current = ll.head
	while current:
		runner = current
		while runner.next:
			if runner.next.value == current.value:
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next
	
	return ll

if __name__ == "__main__":
	ll = MyLinkedList()
	ll = ll.generate(30, 10, 30)
	print("Before Removal: " + str(ll))
	ll = remove_dups_followup(ll)
	print("After Removal: " + str(ll))
