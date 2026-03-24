'''Can you get the loop ? kata'''
def loop_size(node):
    '''
    Finds the size of the loop in linked lists
    using fast and slow pattern.
    '''
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            move = slow.next
            count = 1
            while move != slow:
                move = move.next
                count += 1
            return count
    return None
