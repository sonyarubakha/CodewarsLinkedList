'''Linked Lists - Push & BuildOneTwoThree kata'''
class Node:
    '''
    Node class.
    '''
    def __init__(self, data):
        '''
        Initializes the node.
        '''
        self.data = data
        self.next = None


def push(head, data):
    '''
    Adds new node on the beginning of linked list.
    '''
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    '''
    Creates and returns a linked list like 1 -> 2 -> 3 -> None
    '''
    res = None
    res = push(res, 3)
    res = push(res, 2)
    res = push(res, 1)
    return res
