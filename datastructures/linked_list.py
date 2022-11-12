# linked_list.py
#
# Implementation of a Node class and a Singly Linked List

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value=None):
        print(f'Create list with: {value}')
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
    def insert_first(self, new_value):
        print(f'Insert first: {new_value}')
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def print(self):
        string = "<head> "
        head_node = self.get_head_node()
        current_node = head_node
        while current_node:
            if current_node.get_value():
                if current_node != head_node:
                    string += " -> "
                string += str(current_node.get_value())
            current_node = current_node.get_next_node()
        print("Linked list:", string, "<tail>")
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            current_node = current_node.get_next_node()
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
    
    def remove_head(self):
        current_node = self.get_head_node()
        if current_node:
            next_node = current_node.get_next_node()
            if next_node:
                self.head_node = next_node

    def swap_nodes(self, val1, val2):
        pass


# Todos:
# Remove all Nodes of a kind
# Swap two nodes
# Two Pointers (nth to last)
# Two Pointers (Find the middle left-weighted and right-weighted)
# Find cycle in linked list
# Rotate list by k places





ll = LinkedList()
ll.insert_first(10)
ll.insert_first(20)
ll.insert_first(35)
ll.insert_first(55)
ll.insert_first(71)
ll.print()
ll.remove_head()
ll.print()

