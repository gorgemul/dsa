from collections import defaultdict

init_graph = defaultdict(list, {7: [1], 4: [7], 1: [4], 9: [7, 3], 6: [9], 8: [6, 5], 2: [8], 5: [2], 3: [6]})

class Graph:
    def __init__(self, graph):
        self.graph = graph
    def add_edge(self, tail, head):
        self.graph[tail].append(head)
    def transpose(self):
        transpose_graph = Graph(defaultdict(list))
        for tail, heads in self.graph.items():
            for head in heads:
                transpose_graph.add_edge(head, tail)
        return transpose_graph
    def find_finish_time(self, vertex, visited, time_stack):
        visited.add(vertex)
        for head in self.graph[vertex]:
            if head not in visited:
                self.find_finish_time(head, visited, time_stack)
        time_stack.append(vertex)
    def get_scc(self, vertex, visited, scc):
        scc.append(vertex)
        visited.add(vertex)
        for head in self.graph[vertex]:
            if head not in visited:
                self.get_scc(head, visited, scc)

if __name__ == "__main__":
    graph = Graph(init_graph)
    transpose_graph = graph.transpose()
    visited = set()
    time_stack = []
    for vertex in transpose_graph.graph.keys():
       if vertex not in visited:
           transpose_graph.find_finish_time(vertex, visited, time_stack)
    visited = set()
    sccs = []
    while len(time_stack) > 0:
       scc = []
       vertex = time_stack.pop()
       if vertex not in visited:
           graph.get_scc(vertex, visited, scc)
           sccs.append(scc)
    print(sccs)
