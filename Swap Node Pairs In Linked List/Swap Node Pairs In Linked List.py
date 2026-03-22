class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    bufer = Node()
    bufer.next = head
    prev = bufer
    while prev.next and prev.next.next:
        one = prev.next
        two = prev.next.next
        prev.next = two
        one.next = two.next
        two.next = one
        prev = one
    return bufer.next
