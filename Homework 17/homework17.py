# Linked list: Insert and Remove Value

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at(self, index, data):
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        while current_node is not None and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            print("Index is out of bounds.")
            return

        new_node.next = current_node.next
        current_node.next = new_node



    def remove_value(self, value):
        current_node = self.head

        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return
        

        prev_node = None
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next

        
        if current_node is None:
            print(f"Value {value} not found!")
            return

       
        prev_node.next = current_node.next
        current_node = None


    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next


linked_list = LinkedList()
linked_list.insert_at(0, 10)
linked_list.insert_at(1, 5)
linked_list.insert_at(2, 20)
linked_list.insert_at(2, 100)
linked_list.display()
print()

linked_list.remove_value(5)
linked_list.display()

