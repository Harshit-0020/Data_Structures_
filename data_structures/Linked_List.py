class Node:
    """A representation of the node of a linked list"""

    def __init__(self, data):
        self.data = data
        self.next_node = None

    # This function is called whenever we use a print call and returns the data stored in the node.
    """However the downside is it has to convert all the data into the string dtype."""
    """# Otherwise, it would return the node object and its address.
    def __repr__(self):
        return str(self.data)"""


class LinkedList:
    """A representation of the linked list data structure."""

    def __init__(self):

        # We have access to the head node EXCLUSIVELY!!! and no other node
        # ,so we always have to start with the head node

        self.head = None    # This is the head node OBJECT.

        # This represents the head node of the linked list,
        # first we initialise a linked list with no head node and pointing to null

        self.num_of_nodes = 0

    #   Insert data to the beginning of the linked list.
    #   O(1) - constant running time complexity as we have to just update a bunch of addresses.
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # the head is null so the data structure is EMPTY.
        if self.head is None:
            self.head = new_node
            new_node.next_node = None

        # this is when the linked list is not empty.
        else:
            # We have to update the references.
            new_node.next_node = self.head
            self.head = new_node

    #   O(N) linear running time complexity
    #   because of the while loop, or to find the last node.
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # Check if the linked list is empty or not.
        if self.head is None:
            # new_node.next_node = None -- No need to do this as default next node for node object is None.
            self.head = new_node

        else:
            actual_node = self.head

            # This is why it has O(N) linear running time complexity.
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # We know that the actual node now is the last node,
            # so we insert our new node after the actual node.
            actual_node.next_node = new_node
            new_node.next_node = None

    # O(N) - linear running time complexity.
    def remove(self, data):
        actual_node = self.head

        # We have to keep track of previous node because we cannot
        # go from one node to previous node in singly linked list,
        # and we would have to update the previous node in order to remove the current node.
        previous_node = None

        # Traversing through the list:
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # Search miss
        if actual_node is None:
            return

        # Update the references (so we have the data we would like to remove)
        # Data is at the head:
        if previous_node is None:
            self.head = actual_node.next_node   # Fancy way of saying self.head = None
            self.num_of_nodes -= 1

        # We would like to remove an intermediate node:
        # We don't have to remove the actual node as GARBAGE COLLECTOR will remove it automatically,
        # because there is no active reference to the actual node object
        else:
            previous_node.next_node = actual_node.next_node
            self.num_of_nodes -= 1

    # This is how we get the size of the linked list in O(1) running time complexity.
    def size_of_the_list(self):     # O(1) - constant running time complexity.
        # Returns the number of nodes in the linked list.
        return self.num_of_nodes

    #   O(N) linear running time complexity.
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            # print(type(actual_node.data)) -- This line shows that linked list can return and store data in amy type.
            actual_node = actual_node.next_node


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_end('Harshit')
    linked_list.insert_end(80)
    linked_list.insert_end('Remove this one!')
    linked_list.traverse()
    print(f"Number of nodes: {linked_list.num_of_nodes}")
    print('-' * 25)
    linked_list.remove(500)
    linked_list.traverse()
    print(f"Number of nodes: {linked_list.num_of_nodes}")
