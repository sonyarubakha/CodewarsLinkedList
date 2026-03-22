'''Swap Node Pairs In Linked List kata'''
class Node:
    '''
    Node class.
    '''
    def __init__(self, next=None):
        '''
        Initializes the node.
        '''
        self.next = next

def swap_pairs(head):
    '''
    Swaps nodes in pairs.
    '''
    bufer = Node()
    bufer.next = head
    prev = bufer
    while prev.next and prev.next.next:
        one = prev.next
        two = prev.next.next
        prev.next = two
        one.next = two.next
        two.next = one
        prev = one
    return bufer.next
