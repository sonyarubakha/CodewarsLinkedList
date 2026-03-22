'''Linked Lists - Recursive Reverse kata'''
class Node(object):
    '''
    Node class.
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    '''
    recursively reverses a linked list
    '''
    if not head or not head.next:
        return head
    new = reverse(head.next)
    head.next.next = head
    head.next = None
    return new
