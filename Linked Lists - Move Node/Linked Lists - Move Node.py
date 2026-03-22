class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if not source:
        raise ValueError
    move = source
    source_head = source.next
    move.next = dest
    dest_head = move
    return Context(source_head, dest_head)
