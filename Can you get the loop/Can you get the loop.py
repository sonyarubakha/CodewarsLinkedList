def loop_size(node):
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
