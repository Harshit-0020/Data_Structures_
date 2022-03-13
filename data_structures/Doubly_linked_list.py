class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0
    # By default, insertion in doubly linked list takes place at the end of the list
    # So this function also inserts the new node at the end of the list.

    def insert(self, data):     # O(1) - constant running time complexity.

        new_node = Node(data)
        self.num_of_nodes += 1
        if self.head is None:   # The list is empty:
            self.head = new_node    # Both the head and the tail point to the new node.
            self.tail = new_node    # This means the new node is both head node and tail node.

        else:                   # There is at least one item in the data structure

            self.tail.next_node = new_node  # We don't need to update the next node of new node as it is already null.
            new_node.previous_node = self.tail  # We only update the previous node.
            self.tail = new_node            # Then set the tail node to be new node.

    # This is the huge advantage of the doubly linked lists
    # that we can move in BOTH DIRECTIONS.

    # Traversing in forward direction:
    def traverse_forward(self):
        current_node = self.head

        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.next_node

    # Traversing in backwards direction:
    def traverse_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.previous_node


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(50)
    doubly_linked_list.insert(60)
    doubly_linked_list.insert(70)
    doubly_linked_list.insert(80)
    doubly_linked_list.insert(90)
    doubly_linked_list.insert(100)
    doubly_linked_list.traverse_forward()
    print(f"Total number of nodes: {doubly_linked_list.num_of_nodes}")
    print('-' * 25)
    doubly_linked_list.traverse_backward()
    print(f"Total number of nodes: {doubly_linked_list.num_of_nodes}")
