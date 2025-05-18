class BTreeNode():
  def __init__(self, t):
    self.keys = []
    self.children = []
    self.leaf = True
    self.t = t

  def split(self, parent, value):
    new_node = BTreeNode(self.t)
    
    split_key = self.keys[self._size // 2]
    parent.add_key(split_key) # Key we split on goes to parent

    # New node (same level)
    new_node.children = self.children[self._size // 2 + 1:] # new node get's right children of current node
    new_node.keys = self.keys[self._size // 2 + 1:]

    # Update current node
    self.children = self.children[:self._size // 2 + 1] # current node get's left children of current node
    self.keys = self.keys[:self._size // 2] # not plus one because that went to parent

    parent.children = parent.add_child(new_node)

    # return correct node to go down
    if value < split_key:
      return self
    return new_node

  @property
  def _is_leaf(self):
    return len(self.children) == 0

  @property
  def _is_full(self):
    return self._size == 2 * self.t - 1

  @property
  def _size(self):
    return len(self.keys)

  def add_key(self, value):
    for i in range(len(self.keys)):
      if value < self.keys[i]:
        self.keys.insert(i, value)
    else:
      self.keys.append(value)

  def add_child(self, new_node):
    new_node_first_key = new_node.keys[0]
    for i in range(len(self.children)):
      if new_node_first_key < self.children[i].keys[0]:
        return self.children[:i] + [new_node] + self.children[i:]

    return self.children + [new_node] 

class BTree:
  def __init__(self, t):
    self.t = t
    self.root = BTreeNode(t)

  def find_correct_child_node(self, node, value):
    i = 0
    while i < node._size and value > node.keys[i]:
      i += 1
    return node.children[i]

  def insert(self, value):
    node = self.root

    if node._is_full: # If root is full, we need a new root
      new_root = BTreeNode(self.t)
      new_root.children.append(self.root) # New root get's old root as child
      node = node.split(new_root, value) # Split old root  
      self.root = new_root # Set new root

  # Find spot for value
    while node._is_leaf is False:
      child_node = self.find_correct_child_node(node, value)
      if child_node._is_full: # split ahead of time
        node = child_node.split(node, value)
      else:
        node = child_node
        
    node.add_key(value)
  
  def search(self, value, node=None):
    if node is None:
      node = self.root
        
    if value in node.keys:
      return True
    elif node._is_leaf is True:
      return False # Can't go any deeper
    else:
      child_node = self.find_correct_child_node(node, value)
    return self.search(value, child_node)


btree = BTree(2)
btree.insert(2)
btree.insert(3)
btree.insert(4)
btree.insert(5)
btree.insert(6)
btree.insert(1)
btree.insert(7)
btree.insert(8)
btree.insert(9)
btree.insert(10)
btree.insert(11)
btree.insert(12)
btree.insert(13)

print("Values in root node:", btree.root.keys)
print("    Root's child nodes:", btree.root.children)

for rootchild in btree.root.children:
  print("    Root's child:", rootchild)
  print("    Values in root's child:", rootchild.keys)
  if rootchild.children:
    print("    Child:", rootchild)
    print("        Children to root's child:", rootchild.children)
    for childschild in rootchild.children:
      print("        Values in root's child node:", childschild.keys)




target_value = 10
print("Target value", target_value, "exists:", btree.search(target_value))
