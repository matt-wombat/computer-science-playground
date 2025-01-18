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


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  stations = {
    'Ostbahnhof': ['Max-Weber-Platz', 'Marienplatz'],
    'Marienplatz': ['Ostbahnhof', 'Odeonsplatz', 'Karlsplatz'],
    'Karlsplatz': ['Marienplatz', 'Hauptbahnhof', 'Odeonsplatz'],
    'Hauptbahnhof': ['Karlsplatz'],
    'Odeonsplatz': ['Marienplatz','Max-Weber-Platz','Karlsplatz'],
    'Max-Weber-Platz': ['Odeonsplatz','Ostbahnhof','Arabellapark'],
    'Arabellapark': ['Max-Weber-Platz']
  }

  for val in stations.keys():
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v1 = vertices[v]

    for station in stations[v1.value]:
      for vertex in vertices:
        if vertex.value == station:
          g.add_edge(v1, vertex)
          break

  print_graph(g)

build_graph(False)
