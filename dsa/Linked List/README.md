# Introduction
 linked list.

A linked list is a linear data structure that includes a series of connected elements. Each element of a linked list is called a node.

A node stores data and the address of the next node.

Node in a Linked List
Figure: Node in a Linked List
Here,

data - value of a node
next - address of the next node
Linked List

A linked list is a series of connected nodes.

The first node is the starting point of a linked list and is called the head of that linked list.

The address of the last node must point to None (null), as there are no elements after it.

Real-Life Analogy
Imagine playing a game of Treasure Hunt, where you follow a trail of clues connecting one piece of information to the next until you finally reach the treasure.

A linked list is analogous to this trail of connected clues. And each clue (node) has

a piece of information (data)
a hint to find the next clue (address of the next node)

Time Complexity
Traversing a linked list involves taking a number of steps equal to the number of elements in the list, resulting in a linear time complexity.

Time Complexity: O(n).