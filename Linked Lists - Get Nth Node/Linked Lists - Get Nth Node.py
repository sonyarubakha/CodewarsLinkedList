'''Linked Lists - Get Nth Node kata'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        '''
        Initializes the node.
        '''
        self.data = data
        self.next = next

def get_nth(node, index):
    '''
    Gets node by index(if it is valid)
    '''
    if index < 0 or node is None:
        raise ValueError('Invalid index')
    now = node
    while now:
        if index == 0:
            return now
        now = now.next
        index -= 1
    raise ValueError('Invalid index')
