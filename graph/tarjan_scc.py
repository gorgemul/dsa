from collections import defaultdict

init_graph = defaultdict(list, {7: [1], 4: [7], 1: [4], 9: [7, 3], 6: [9], 8: [6, 5], 2: [8], 5: [2], 3: [6]})

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.vertex_info = { vertex: { "index": -1, "lowlink": -1 } for vertex in graph}
        self.index = 0
        self.stack = []
        self.sccs = []
    def get_sccs_recursive(self, u):
        self.vertex_info[u]["index"] = self.index
        self.vertex_info[u]["lowlink"] = self.index
        self.index += 1
        self.stack.append(u)
        for v in self.graph[u]:
            if self.vertex_info[v]["index"] == -1:
                self.get_sccs_recursive(v)
                self.vertex_info[u]["lowlink"] = min(self.vertex_info[u]["lowlink"], self.vertex_info[v]["lowlink"])
            elif v in self.stack:
                self.vertex_info[u]["lowlink"] = min(self.vertex_info[u]["lowlink"], self.vertex_info[v]["index"])
        if self.vertex_info[u]["index"] == self.vertex_info[u]["lowlink"]:
            scc = []
            while True:
                v = self.stack.pop()
                scc.append(v)
                if v == u:
                    break
            self.sccs.append(scc)
    def get_sccs(self):
        for u in self.graph:
            if self.vertex_info[u]["index"] == -1:
                self.get_sccs_recursive(u)
        return self.sccs
