class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    info = list_repr.split(' -> ')
    info = info[:-1]
    if not info:
        return None
    head = Node(int(info[0]))
    now = head
    for el in info[1:]:
        now.next = Node(int(el))
        now = now.next
    return head
