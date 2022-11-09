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
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
    def insert_first(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def stringify(self):
        string = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                if string:
                    string += " -> "
                string += str(current_node.get_value())
            current_node = current_node.get_next_node()
        return string
    
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



ll = LinkedList(10)
ll.insert_first(20)
ll.insert_first(35)
ll.insert_first(55)
ll.insert_first(71)

print(ll.stringify())
