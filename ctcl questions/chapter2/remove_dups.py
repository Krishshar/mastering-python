from LinkedList import LinkedList

def remove_dups(ll):
	if ll.head is None:
		return

	current = ll.head
	seen = set([current.value])
	while current.next:
		if current.next.value in seen:
			current.next = current.next.next
		else:
			seen.add(current.next.value)
			current = current.next
	return ll

# Using runner
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

	return ll.head

if __name__ == '__main__':
	ll = LinkedList()
	ll.generate(100, 0, 9)
	print(f"Before: {ll}")
	remove_dups(ll)
	print(f"After: {ll}")

	ll.generate(100, 0, 9)
	print(f"Before: {ll}")
	remove_dups_followup(ll)
	print(f"After: {ll}")