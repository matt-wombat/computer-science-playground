#
#
#  Warning: It is unclear, if this implementation is correct.
#
#


import random
from random import randrange
from graph import Graph
from vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsm_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:
def all_vertices_visited(vertex_visited):
  for vertex in vertex_visited:
    if not vertex_visited[vertex]:
      return False
  return True

def traveling_salesman(graph):
  traveling_salesman_path = ''

  # Dictionary holding a status of all vertices and if there already been visited
  vertex_visited = {x: False for x in graph.graph_dict}

  # Diese Implementierung noch checken ob graph.graph_dict.keys() das gleiche ausgibt, wie list(graph.graph_dict)
  # current_vertex = random.choice(graph.graph_dict.keys())
  curr_vertex = random.choice(list(graph.graph_dict))
  # curr_vertex = 'a'
  vertex_visited[curr_vertex] = True
  traveling_salesman_path += curr_vertex

  # Alle Knoten geprüft?
  all_visited = all_vertices_visited(vertex_visited)

  # While not all vertices are visited:
  while not all_visited:

    # Create dictinary of all vertices connected to the current vertex with their weights.
    curr_vertex_edges = graph.graph_dict[curr_vertex].get_edges()
    curr_vertex_edge_weights = {}
    for edge in curr_vertex_edges:
      curr_vertex_edge_weights[edge] = graph.graph_dict[curr_vertex].get_edge_weight(edge)
    
    next_found = False
    next_vertex = ''

    # Loop to run as long as the next vertex HAS NOT been found
    while not next_found:
      if curr_vertex_edge_weights is None:
        break
      
      # Select the minimum weight edge from the dictionary and check whether it points to a vertex that has already been visited or not. If unvisited, we have found our next_vertex. If visited, pop the edge from our dictionary and continue searching.

      next_vertex = min(curr_vertex_edge_weights, key=curr_vertex_edge_weights.get)
      if vertex_visited[next_vertex]:
        curr_vertex_edge_weights.pop(next_vertex)
      else:
        next_found = True
      
      # If dictionary of current vertex edge weights is empty break from the process of finding next vertices
      if curr_vertex_edge_weights is None:
        all_visited = True

      # else: set the current vertex to be the next vertex and mark it as visited and add it to the Traveling Salesman Path
      else:
        curr_vertex = next_vertex
        vertex_visited[curr_vertex] = True
        traveling_salesman_path += curr_vertex

    # Check if all vertices were visited
    all_visited = all_vertices_visited(vertex_visited)

  print(traveling_salesman_path)


graph = build_tsm_graph(False)
traveling_salesman(graph)

        
      
      