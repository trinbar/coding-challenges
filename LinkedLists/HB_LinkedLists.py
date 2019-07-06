# Given a linked list Node class, create a singly-linked Linked List class with
#  2 methods: __init__ and append. Given node class:
class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Linked List class."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,node):
        self.tail.next = node
        self.tail = node

# Assuming you have a LinkedList class with a __init__ method, 
#  add a method called print_list that prints out the data for each node in the 
#  linked list, in order. This method should return None.

    def print_list(self):
        """Prints each node in the LinkedList. Returns None."""

        current = self.head

        #while loop that checks if current exists
        while current:
            #if current exists, print current
            print(current)
            #traverse LinkedList by reassigning current to current.next
            current = current.next

# Assuming you have a LinkedList class with a __init__ method, create a method
#  called pop that removes the last node from the LinkedList and also returns it.
#  Recall that this is a singly-linked list.
    
    def pop(self):
        """Removes the last node from the LinkedList and returns it."""

        #Start at head
        current = self.head

        #Reassign second to last node's pointer to None

        #while loop that checks if next two nodes exist
        while current.next.next:
            #traverse LinkedList by reassigning current to current.next
            current = current.next

        #when current.next.next no longer exists

        #reassign the tail to current.next
        self.tail = current.next

        #Return original tail
        return current.next.next

# Create a Node class for a doubly-linked list. Then, create the append method 
# for a doubly-linked LinkedList class.

# [Harder] Assuming you have a LinkedList class with a __init__ method, create a
#  method called print_odd_nodes which prints nodes with odd indices (1, 3, 5, 7, ... until end).

# [Harder] Create a method for a singly-linked LinkedList class called has_consecutive_repeat that returns True or False, depending on whether there are two nodes with the same value that are consecutive. (i.e. Node with data 2 directly followed by another Node with data 2.)
# [Harder] Create a method for a doubly-linked list called insert which takes an index number and a piece of data as parameters. The method should create a new Node using the given data, and mutate the doubly-linked list to add the new node at the given index.