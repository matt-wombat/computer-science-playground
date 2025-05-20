class Hamiltonian:
  def __init__(self, vertices, adjacency_matrix, starting_vertex):
    # Store the vertices
    self.vertices = vertices

    # Store the adjacency_matrix
    self.adj_matrix = adjacency_matrix

    # Store the starting_vertex
    self.start = starting_vertex

    # Create a list to hold the current path
    self.path = []

    # Create a list to hold all visited vertices, where
    # 0 means not visited, and 1 means visited. To start out, all vertices are 0.
    self.visited_vertices = [0 for x in range(len(self.vertices))]

    # Create a list that stores all Hamiltonian paths
    self.hpaths = []
    # Create a list that stores all Hamiltonian cycles
    self.cycles = []

    self.num_vertices = len(self.vertices)

  def traverse(self):
    # Add the starting vertex to the path list
    # Add code below
    self.path.append(self.start)
    # Start the recursive search on the first vertex to find the path and cycle if they exist
    # Add code below (remove the pass)
    self.search(self.start)

  def search(self, vertex):
    # First check for the exit condition: 
    # Check if all vertices have been visited
    all_visited = True
    for i in range(1, len(self.visited_vertices)):
      if self.visited_vertices[i] == 0:
        all_visited = False
        break
    # Check that every vertex was visited and there are no duplicate visited vertices -> this is a Hamiltonian path
    if all_visited and len(self.path) == len(set(self.path)):
      # Append the path to the hpaths list. Since the path variable will be modified, create a deep copy of the list before appending it.
      self.hpaths.append(list(self.path))
    # Check if cycle exists
    # If the current vertex equals the starting vertex AND the path length equals the number of vertices plus one (since the starting node will be in the path twice)
    if vertex == self.start and len(self.path) == self.num_vertices + 1:
      # Append the path to the cycles list. Since the path variable will be modified, create a deep copy of the list before appending it.
      self.cycles.append(list(self.path))
      
      return
    # Step through each vertex
    for neighbor in range(len(vertices)):
      # See if this neighbor is connected to
       # vertex and has not been previously visited
      if self.adj_matrix[vertex][neighbor] == 1 and self.visited_vertices[neighbor] == 0:
        # Set this neighbor index within visited_vertices to 1
        # Add code below
        self.visited_vertices[neighbor] = 1
        # Add this neighbor to the path
        # Add code below
        self.path.append(neighbor)

        # Traverse the neighbor to continue finding the path
        self.search(neighbor)
        # Backtrack
        # Set the neighbor index in visited_vertices back to 0
        # Add code below
        self.visited_vertices[neighbor]=0
        # Pop the neighbor from the path
        # Add code below
        self.path.pop()


if __name__ == '__main__':
  vertices = ['School', 'Sanjay', 'Marquis', 'Marisol', 'Lisa']
  adjacency_matrix = [
                      [0, 1, 0, 0, 1],
                      [1, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1],
                      [1, 0, 0, 1, 0]
                    ]
  # adjacency_matrix2 = [
  #                     [0, 1, 1, 0, 0], 
  #                     [1, 0, 1, 0, 0], 
  #                     [1, 1, 0, 1, 0], 
  #                     [0, 0, 1, 0, 1], 
  #                     [0, 0, 0, 1, 0]  
  #                   ]

  hamilton = Hamiltonian(vertices, adjacency_matrix, 0)
  #hamilton = Hamiltonian(vertices, adjacency_matrix2, 0)

  hamilton.traverse()
  print("Hamiltonian paths:" + str(hamilton.hpaths))
  print("Hamiltonian cycles:" + str(hamilton.cycles))