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
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value():
                if current_node != self.get_head_node():
                    string += " -> "
                string += str(current_node.get_value())
            current_node = current_node.get_next_node()
        print("Linked list:", string, "<tail>")
    
    def remove_node(self, value_to_remove, remove_all=False):
        occurence = 'all nodes' if remove_all else 'first node'
        print(f'Removing {occurence}: {value_to_remove}')
        current_node = self.get_head_node()

        removed = False
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            removed = True
        
        if not remove_all and removed:
            return

        more_nodes = True
        while more_nodes:
            next_node = current_node.get_next_node()
            
            if next_node:
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    if not remove_all:
                        more_nodes = False
                    removed = True
                else:
                    current_node = next_node
            else:
                more_nodes = False
        
        if not removed:
            print(f'Removing not possible: {value_to_remove} not in list')
    
    def remove_head(self):
        current_node = self.get_head_node()
        print(f'Removing head: {current_node.get_value()}')
        if current_node:
            next_node = current_node.get_next_node()
            if next_node:
                self.head_node = next_node

    def swap_first_nodes(self, val1, val2):
        if val1 == val2:
            print(f"Swapping not necessary: {val1} and {val2} are equal")
            return

        print(f"Swapping first occurences: {val1} <-> {val2}")

        node1_prev = None
        node1 = self.get_head_node()
        node2_prev = None
        node2 = self.get_head_node()

        # Find nodes which should be swapped
        while node1 is not None:
            if node1.get_value() == val1:
                break
            else:
                node1_prev = node1
                node1 = node1.get_next_node()
        
        while node2 is not None:
            if node2.get_value() == val2:
                break
            else:
                node2_prev = node2
                node2 = node2.get_next_node()
        
        messageStr = "Swapping not possible: {} not in list"
        if node1 is None:
            print(messageStr.format(val1))
        if node2 is None:
            print(messageStr.format(val2))
        if node1 is None or node2 is None:
            return

        # Swap head node or previous node with the opposite node
        if node1_prev == None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev == None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # Swap references to next node in both nodes using temporary node
        node1_next_temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(node1_next_temp)

    def nth_to_last(self, nth):
        tail = self.get_head_node()
        nth_to_last_node = self.get_head_node()
        counter = 1

        while tail.get_next_node():
            tail = tail.get_next_node()
            if counter >= nth + 1:
                nth_to_last_node = nth_to_last_node.get_next_node()
            counter += 1

        print(f"{nth} to last node: {nth_to_last_node.get_value()}")


# Todos:
# Two Pointers (Find the middle left-weighted and right-weighted)


ll = LinkedList()
ll.insert_first(11)
ll.insert_first(20)
ll.insert_first(10)
ll.insert_first(35)
ll.insert_first(10)
ll.insert_first(55)
ll.insert_first(10)
ll.insert_first(71)
ll.print()
ll.remove_head()
ll.print()
ll.swap_first_nodes(55, 55)
ll.swap_first_nodes(81, 63)
ll.swap_first_nodes(35, 20)
ll.print()
ll.swap_first_nodes(10, 55)
ll.print()
ll.swap_first_nodes(20, 55)
ll.print()
ll.swap_first_nodes(20, 11)
ll.print()
ll.swap_first_nodes(20, 10)
ll.print()
ll.remove_node(10)
ll.print()
ll.remove_node(10, True)
ll.print()
ll.remove_node(10)
ll.print()
ll.nth_to_last(3)


