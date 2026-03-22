class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0 or node is None:
        raise ValueError('Invalid index')
    now = node
    while now:
        if index == 0:
            return now
        now = now.next
        index -= 1
    raise ValueError('Invalid index')
