def stringify(node):
    res = []
    while node is not None:
        res.append(str(node.data))
        node = node.next
    res.append('None')
    return ' -> '.join(res)
