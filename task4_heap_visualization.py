"""Завдання 4. Побудова дерева з бінарної купи та її візуалізація."""
import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())


def heap_to_tree(values):
    """Перетворює список, що представляє min-heap, на звичайне бінарне дерево."""
    if not values:
        return None
    nodes = [Node(value) for value in values]
    for i, node in enumerate(nodes):
        left_index, right_index = 2 * i + 1, 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]
    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return
    graph.add_node(node.id, label=str(node.val))
    if node.left:
        graph.add_edge(node.id, node.left.id)
        left_x = x - 1 / (2 ** layer)
        pos[node.left.id] = (left_x, y - 1)
        add_edges(graph, node.left, pos, left_x, y - 1, layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / (2 ** layer)
        pos[node.right.id] = (right_x, y - 1)
        add_edges(graph, node.right, pos, right_x, y - 1, layer + 1)


def visualize_heap(heap_values):
    if not heap_values:
        print("Купа порожня.")
        return
    root = heap_to_tree(heap_values)
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)
    labels = {node_id: data["label"] for node_id, data in graph.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False,
            node_size=2200, node_color="lightblue", font_size=11)
    plt.title("Візуалізація бінарної min-heap")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    numbers = [7, 2, 9, 1, 5, 3, 8, 4]
    heapq.heapify(numbers)
    print("Масив купи:", numbers)
    visualize_heap(numbers)
