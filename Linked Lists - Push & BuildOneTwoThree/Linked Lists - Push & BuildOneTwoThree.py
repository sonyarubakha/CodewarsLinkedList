
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    res = None
    res = push(res, 3)
    res = push(res, 2)
    res = push(res, 1)
    return res
