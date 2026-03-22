
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new = Node(data)
    if not head or new.data < head.data:
        new.next = head
        return new
    now = head
    while now.next and now.next.data < data:
        now = now.next
    new.next = now.next
    now.next = new
    return head
