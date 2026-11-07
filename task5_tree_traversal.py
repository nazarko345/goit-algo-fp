"""Завдання 5. Ітеративні DFS і BFS з покроковою кольоровою візуалізацією."""
import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())


def build_sample_tree():
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.left.left, root.left.right = Node(4), Node(5)
    root.right.left, root.right.right = Node(6), Node(7)
    return root


def collect_graph(root):
    graph = nx.DiGraph()
    positions, labels = {}, {}
    queue = deque([(root, 0, 0)])
    while queue:
        node, x, y = queue.popleft()
        graph.add_node(node.id)
        labels[node.id] = str(node.value)
        positions[node.id] = (x, -y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            queue.append((node.left, x - 1 / (2 ** (y + 1)), y + 1))
        if node.right:
            graph.add_edge(node.id, node.right.id)
            queue.append((node.right, x + 1 / (2 ** (y + 1)), y + 1))
    return graph, positions, labels


def traversal_order(root, method="bfs"):
    """Повертає порядок обходу. BFS використовує чергу, DFS — стек."""
    order = []
    if root is None:
        return order

    if method.lower() == "bfs":
        container = deque([root])
        while container:
            node = container.popleft()
            order.append(node.id)
            if node.left:
                container.append(node.left)
            if node.right:
                container.append(node.right)
    elif method.lower() == "dfs":
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node.id)
            # Спочатку додаємо правого, щоб лівий обробився першим.
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    else:
        raise ValueError("method має бути 'bfs' або 'dfs'")
    return order


def visualize_traversal(root, method="bfs"):
    graph, pos, labels = collect_graph(root)
    order = traversal_order(root, method)
    total = max(len(order) - 1, 1)
    cmap = plt.cm.Blues
    for step, visited_id in enumerate(order, start=1):
        colors = []
        for node_id in graph.nodes:
            if node_id in order[:step]:
                visit_index = order.index(node_id)
                shade = 0.25 + 0.7 * (visit_index / total)
                colors.append(cmap(shade))
            else:
                colors.append("#D9D9D9")
        plt.figure(figsize=(9, 5))
        nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False,
                node_size=1800, node_color=colors, font_size=11)
        plt.title(f"{method.upper()} — крок {step}: відвідано вузол {labels[visited_id]}")
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    print(f"Порядок {method.upper()}:", " -> ".join(labels[node_id] for node_id in order))


if __name__ == "__main__":
    tree = build_sample_tree()
    visualize_traversal(tree, "dfs")
    visualize_traversal(tree, "bfs")
