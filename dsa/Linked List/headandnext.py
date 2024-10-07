class Node:
    def __init__(self, data):
        self.data = data

        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None


    def create_LinkedList(self):
        node1 = Node(22)
        self.head = node1

        node2 = Node(33)
        node1.next = node2

        node3 = Node(55)
        node2.next = node3

        node3.next = None

    def traverse_linked_list(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

linked_list = LinkedList()

linked_list.create_LinkedList()

linked_list.traverse_linked_list()