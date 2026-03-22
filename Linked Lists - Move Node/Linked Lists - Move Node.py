'''Linked Lists - Move Node kata'''
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

class Context(object):
    '''
    Context class.
    '''
    def __init__(self, source, dest):
        '''
        Initializes the context object.
        '''
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''
    takes the node from the front of the source list
    and moves it to the front of the destintation list.
    '''
    if not source:
        raise ValueError
    move = source
    source_head = source.next
    move.next = dest
    dest_head = move
    return Context(source_head, dest_head)
