from collections import defaultdict
import algorytm_trojkat_silowy as ts


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)

    return path


g = Graph()
data = ts.get_data(ts.very_easy)
print(data)
for row in range(len(data)):
    for el in range(len(data[row])):
        g.add_node((row, el))
for row in range(len(data) - 1):
    for el in range(len(data[row])):
        g.add_edge((row, el), (row + 1, el), data[row + 1][el])
        g.add_edge((row, el), (row + 1, el + 1), data[row + 1][el + 1])

# print(g.nodes)
# print(g.edges)
# print(g.distances)

print(dijkstra(g, (0, 0)))
