#random array
arr = [ 23, 27, 79, 80, 58, 87, 9, 53, 12, 82, 45, 69, 66, 82, 8, 67, 21, 25, 3, 18, 42, 42, 11, 61, 61, 70, 40, 49, 37, 82, 83, 22, 87, 18, 65, 48, 33, 54, 25, 71, 14, 3, 80, 57, 50, 48, 1, 21, 38, 86, 63, 37, 43, 78, 62, 67, 40, 88, 35, 1, 96, 24, 73, 64, 86, 21, 83, 83, 57, 41, 16, 81, 38, 88, 65, 44, 60, 63, 7, 47, 53, 58, 98, 56, 78]

class Node:
    parent = None # equivalent of Null
    right = None
    left = None
    value = None
    def __init__(self, l, r, p, v):
        self.right = r
        self.left = l
        self.parent = p
        self.value = v

def insert_value(value, node):
    if (node.parent == None
        and node.left == None
        and node.right == None
        and node.value == None):
        node.value = value
        return
    else:
        if (node.value <= value):
            if (node.right == None):
                node.right = Node(None, None, node, value)
            else:
                insert_value(value, node.right)
        else:
            if (node.left == None):
                node.left = Node(None, None, node, value)
            else:
                insert_value(value, node.left)
    
def print_nodes(node):
    if node != None:
        print_nodes(node.left)
        print(node.value, end='')
        print(" ", end='')
        print_nodes(node.right)

def search_node(node, value):
    if node != None:
        if node.value == value:
            return node
        elif value >= node.value:
            return search_node(node.right, value)
        else:
            return search_node(node.left, value)
    else:
        return None # the value is not in the tree

def bst_min(node):
    if node.left == None:
        return node
    else:
        return bst_min(node.left)

def bst_max(node):
    if node.right == None:
        return node
    else:
        return bst_min(node.right)

def successor(node):
    if node.right != None:
        return bst_min(node.right)

def predecessor(node):
    if node.left != None:
        return bst_max(node.left)

def delete_node(node):
    if node.left == None and node.right == None:
        # case 1: leaf node
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    elif node.left == None or node.right == None:
        # case 2: node with one child
        if node.left != None:
            child = node.left
        else:
            child = node.right
        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child
        child.parent = node.parent
    else:
        # case 3: node with two children
        succ = successor(node)
        node.value = succ.value
        delete_node(succ)
        

head = Node(None, None, None, None)
