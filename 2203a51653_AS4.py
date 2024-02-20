# Define the tree structure
tree = {
    'A': {
        'B': {'D': -1, 'E': 4},
        'C': {'F': 2, 'G': 6}
    }
}

def min_max(node, maximizing=True):
    if isinstance(node, int):
        return node
    if maximizing:
        return max(min_max(child, False) for child in node.values())
    else:
        return min(min_max(child, True) for child in node.values())

result = min_max(tree['A'])
print(f"The optimal value is: {result}")
