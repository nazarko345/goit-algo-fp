"""Завдання 3. Алгоритм Дейкстри з бінарною купою (heapq)."""
import heapq
from math import inf


def dijkstra(graph: dict, start):
    """Повертає словник найкоротших відстаней і попередників."""
    if start not in graph:
        raise ValueError(f"Початкової вершини {start!r} немає у графі.")

    distances = {vertex: inf for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if current_distance != distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            if weight < 0:
                raise ValueError("Алгоритм Дейкстри не працює з від'ємними вагами.")
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous


def restore_path(previous, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous[target]
    return list(reversed(path))


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }
    start = "A"
    distances, previous = dijkstra(graph, start)
    print(f"Найкоротші шляхи від вершини {start}:")
    for vertex, distance in distances.items():
        path = restore_path(previous, vertex) if distance != inf else []
        print(f"{vertex}: відстань = {distance}, шлях = {' -> '.join(path) or 'недосяжна'}")
