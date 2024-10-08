class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 90->80->60->50
    def create_linked_list(self):
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    # display linked list in format: A->B->C
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # method to append a node
    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

linked_list = LinkedList()

# create the initial linked list
linked_list.create_linked_list()

# input for data to append
data = int(input())
linked_list.append(data)

# print the updated linked list
linked_list.display()


#adding git graph
#so how does it look testing