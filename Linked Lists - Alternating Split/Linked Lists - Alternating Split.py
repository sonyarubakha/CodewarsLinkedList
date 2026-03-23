class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError('The list is too short.')
    first = head
    second = head.next
    now_first = first
    now_second = second
    while now_first and now_second:
        now_first.next = now_second.next
        now_first = now_first.next
        if now_first:
            now_second.next = now_first.next
            now_second = now_second.next
    return Context(first, second)
