class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    now = head
    while now and now.next:
        if now.data == now.next.data:
            now.next = now.next.next
        else:
            now = now.next
    return head
