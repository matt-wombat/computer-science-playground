from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
import networkx as nx
import matplotlib.pyplot as plt

# Build your program below:
landmark_string = ''
for (letter, landmark) in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
stations_under_construction = []

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def goodbye():
  print("Thanks for using SkyRoute!")

def skyroute():
  greet()
  vizualize_graph()
  new_route()
  goodbye()


def set_start_and_end(start_point, end_point):
  if start_point:
    change_point = input("What would you like to change? You can enter:\n'o' for 'origin'\n'd' for 'destination'\nor 'b' for 'both'\n:")
    if change_point == "b":
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
  
  return start_point, end_point

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_start()
    

def get_end():
  end_point_letter = input("Where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_end()
  
def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  if shortest_route:
    shortest_route_string = ' -> '.join(shortest_route)
    print(f"The shortest metro route from {start_point} to {end_point} is:\n{shortest_route_string}")
  else:
    print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance.")

  again = input("Would you like to see another route? Enter y/n: ")
  if again == "y":
    show_landmarks()
    new_route(start_point, end_point)


def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      metro_system = get_active_stations() if stations_under_construction else vc_metro
      if stations_under_construction:
        possible_route = dfs(metro_system, start_station, end_station)
        if not possible_route:
          continue
      route = bfs(metro_system, start_station, end_station)
      if route:
        routes.append(route)
  
  if routes:  
    shortest_route = min(routes, key=len)
    return shortest_route



def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == 'y':
    print(landmark_string)

def get_active_stations():
  updated_metro = vc_metro
  for station_unter_construction in stations_under_construction:
    for current_station, neighbors in vc_metro.items():
      if current_station != station_unter_construction:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([])

  return updated_metro

def vizualize_graph():
  G = nx.Graph(vc_metro)
  pos =nx.spring_layout(G, seed = 50)
  nx.draw(G, pos, with_labels = True, node_size = 2000)
  plt.show()



skyroute()






