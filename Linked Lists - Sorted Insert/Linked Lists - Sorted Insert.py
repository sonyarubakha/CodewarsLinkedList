'''Linked Lists - Sorted Insert'''
class Node(object):
    '''
    Node class.
    '''
    def __init__(self, data):
        '''
        Initializes the node.
        '''
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''
    Inserts new node but in a sorted place.
    '''
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
