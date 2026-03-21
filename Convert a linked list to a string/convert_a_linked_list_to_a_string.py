'''Convert a linked list to a string kata'''
def stringify(node):
    '''
    Converts a linked list to a string with data.
    '''
    res = []
    while node is not None:
        res.append(str(node.data))
        node = node.next
    res.append('None')
    return ' -> '.join(res)
