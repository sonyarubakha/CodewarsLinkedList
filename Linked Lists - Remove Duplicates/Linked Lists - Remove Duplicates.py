'''Linked Lists - Remove Duplicates kata'''
class Node(object):
    '''
    Node class.
    '''
    def __init__(self, data):
        '''
        Initializes the node
        '''
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''
    removes duplicates from linked lists.
    '''
    if not head:
        return head
    now = head
    while now and now.next:
        if now.data == now.next.data:
            now.next = now.next.next
        else:
            now = now.next
    return head
