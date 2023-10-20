"""Graph data structures are data structures that consist of a collection of nodes or vertices connected by edges.
Graphs are used to represent relationships or connections between objects and are widely used in various fields,
including computer science, mathematics, social networks, and transportation systems.
"""

from typing import Dict, List
import heapq


class FlightRouteGraph:
    def __init__(self):
        """
        Initialize an empty flight route graph.
        """
        self.graph = {}

    def add_airport(self, airport: str):
        """
        Add an airport to the graph.

        :param airport: The name of the airport.
        """
        if airport not in self.graph:
            self.graph[airport] = []

    def add_flight(self, source: str, destination: str, distance: float):
        """
        Add a flight route to the graph.

        :param source: The source airport.
        :param destination: The destination airport.
        :param distance: The distance between the source and destination.
        """
        if source in self.graph:
            self.graph[source].append((destination, distance))
        else:
            print(f"Airport '{source}' does not exist in the graph.")

    def get_best_route(self, source: str, destination: str) -> List[str]:
        """
        Find the best route (shortest path) between two airports using Dijkstra's algorithm.

        :param source: The source airport.
        :param destination: The destination airport.
        :return: A list of airports representing the best route.
        """
        if source not in self.graph or destination not in self.graph:
            return []

        # Create a priority queue for Dijkstra's algorithm
        queue = [(0, source)]
        distances = {airport: float('inf') for airport in self.graph}
        distances[source] = 0
        previous_airport = {}

        while queue:
            current_distance, current_airport = heapq.heappop(queue)

            if current_distance > distances[current_airport]:
                continue

            for neighbor, weight in self.graph[current_airport]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_airport[neighbor] = current_airport
                    heapq.heappush(queue, (distance, neighbor))

        # Reconstruct the best route
        best_route = []
        current_airport = destination
        while current_airport is not None:
            best_route.insert(0, current_airport)
            current_airport = previous_airport.get(current_airport)

        return best_route

    def __str__(self):
        return str(self.graph)


# Example usage:
flight_graph = FlightRouteGraph()

# Adding airports to the graph
flight_graph.add_airport("JFK")
flight_graph.add_airport("LAX")
flight_graph.add_airport("ORD")
flight_graph.add_airport("DFW")

# Adding flight routes with distances
flight_graph.add_flight("JFK", "LAX", 2000)
flight_graph.add_flight("JFK", "ORD", 800)
flight_graph.add_flight("LAX", "DFW", 1500)
flight_graph.add_flight("ORD", "DFW", 900)

# Find the best route from JFK to DFW
best_route = flight_graph.get_best_route("JFK", "DFW")
print("Best Route from JFK to DFW:", best_route)

# ============================================ Another example =========================================

from collections import deque


def bfs(graph, start, target, return_path=False):
    """
    Perform a Breadth-First Search (BFS) on a graph to find a target city.

    :param graph: The graph represented as a dictionary.
    :param start: The starting city for the search.
    :param target: The city you want to find.
    :param return_path: If True, return the path to the target.
    :return: True if the target is found, or the path to the target if return_path is True, else False.
    """
    visited = set()
    queue = deque([(start, [])])  # Use a tuple to keep track of the path.

    while queue:
        city, path = queue.popleft()
        if city == target:
            if return_path:
                return path + [city]
            return True

        visited.add(city)

        for neighbor in graph.get(city, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [city]))  # Update the path.

    if return_path:
        return []  # Target not found
    return False


# Dictionary mapping abbreviations to city names
city_names = {
    'New York': 'New York',
    'Chicago': 'Chicago',
    'Los Angeles': 'Los Angeles',
    'Dallas': 'Dallas',
    'San Francisco': 'San Francisco',
    'Miami': 'Miami'
}

# Example graph with city names
city_graph = {
    'New York': ['Chicago', 'Los Angeles'],
    'Chicago': ['New York', 'Dallas', 'San Francisco'],
    'Los Angeles': ['New York', 'Miami'],
    'Dallas': ['Chicago'],
    'San Francisco': ['Chicago', 'Miami'],
    'Miami': ['Los Angeles', 'San Francisco']
}

start_city = "San Francisco"
target_city = "Chicago"  # Corrected starting and target cities

result = bfs(city_graph, start_city, target_city, return_path=True)

if result:
    path = [city_names.get(city) for city in result]  # Convert back to full city names
    print(f"Path from {city_names[start_city]} to {city_names[target_city]}: {path}")
else:
    print(f"No path found from {city_names[start_city]} to {city_names[target_city]}")
