class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
        
node = Node(42)
print(node)