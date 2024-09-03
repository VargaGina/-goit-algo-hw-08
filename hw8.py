class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.key

#Exemplu de utilizare
root=Node(20)
root.left=Node(10)
root.right=Node(30)
root.right.right=Node(40)

print("Valoarea maxima in arbore:", find_max(root))

def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.key

#Exemplu de utilizare
root=Node(20)
root.left=Node(10)
root.right=Node(30)
root.left.left=Node(5)

print("Valoarea minima in arbore:", find_min(root))


def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)


#Exemplu de utilizare
root=Node(20)
root.left=Node(10)
root.right=Node(30)
root.left.left=Node(5)
root.right.right=Node(40)

print("Suma tuturor valorilor din arbore:", sum_tree(root))


