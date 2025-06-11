from collections import defaultdict
"""
dijktra shortest path implementation, time complexitiy is m*n, could be optimized by using heap, should implement it later
"""
INF = 1000000

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.path_table = dict()
        self.visited = set()
    def nearestNeighbor(self, node_key):
        min_node = tuple()
        for neighbor_node in self.graph[node_key]:
            if neighbor_node[0] not in self.visited:
                if len(min_node) == 0 or neighbor_node[1] < min_node[1]:
                    min_node = neighbor_node
        return min_node
    def calculate_path(self, src_key, dst_key) -> int:
        if src_key == dst_key: return 0
        self.path_table = { k: 0 if k == src_key else float("inf") for k in self.graph }
        self.visited.add(src_key)
        neighbor = self.nearestNeighbor(src_key)
        if len(neighbor) == 0: return INF
        if neighbor[0] == dst_key: return neighbor[1]
        self.visited.add(neighbor[0])
        self.path_table[neighbor[0]] = neighbor[1]
        return self.calculate_path_recursive(dst_key)
    def calculate_path_recursive(self, dst_key) -> int:
        frontier_min_node = tuple()
        for node_key in self.visited:
            min_node = self.nearestNeighbor(node_key)
            if len(min_node) == 0: continue
            dijkstra_greedy_factor = min_node[1] + self.path_table[node_key]
            if len(frontier_min_node) == 0 or dijkstra_greedy_factor < frontier_min_node[1]:
                frontier_min_node = (min_node[0], dijkstra_greedy_factor)
        if len(frontier_min_node) == 0: return INF
        if frontier_min_node[0] == dst_key: return frontier_min_node[1]
        self.visited.add(frontier_min_node[0])
        self.path_table[frontier_min_node[0]] = frontier_min_node[1]
        return self.calculate_path_recursive(dst_key)
            

if __name__ == "__main__":
    init_graph = defaultdict(list)
    with open("dijkstra_shortest_path_test.txt", "r") as file:
        for line in file:
            line_lst = line.strip().split()
            key = line_lst.pop(0)
            for item in line_lst:
                dst_lst = item.split(",")
                init_graph[key].append((dst_lst[0], int(dst_lst[1])))
    graph = Graph(init_graph)
    print(graph.calculate_path("1", "89"))
