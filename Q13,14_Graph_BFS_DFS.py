class Node(object):
    def __init__(self, value):
        self.vertex = value


class Graph:
    def __init__(self):
        self.edge = []  # list of lists of each nodes possible edges
        self.edge_location = {}  # dictionary of the position of the node within the above dictionary
        self.dfs_path = []  # stores completed path
        self.bfs_path = []  # stores completed path
        self.queue = []  # stores nodes to be checked next

    def add_node(self, x):
        for _list in self.edge:
            _list.append(0)
        self.edge.append([0] * (len(self.edge) + 1))
        self.edge_location[x.vertex] = len(self.edge_location)

        """self.edge[self.edge_location[x] will find the list to be
        updated and [self.edge_location[y] will point to the correct value
        in the list to be updated"""
    def add_edge(self, x, y):
        self.edge[self.edge_location[x]][self.edge_location[y]] = 1
        self.edge[self.edge_location[y]][self.edge_location[x]] = 1

    def display_graph(self):
        s = sorted(self.edge_location.items())
        for node, edge in s:
            print(node + " ", end="|")
            for i in range(len(self.edge)):
                print(self.edge[edge][i], end="")
            print("")

    def dfs(self, graph, start):
        s = sorted(self.edge_location.items())
        a = -1  # to keep track of the position in the list
        if start not in self.dfs_path:  # add start to path
            self.dfs_path.append(start)
        """check for connections to the start node"""
        for i in self.edge[self.edge_location[start]]:
            a += 1
            if i != 0:
                for k, v in s:
                    """if the node is already in the path continues to iterate until
                    a node is found which isn't or until none are found
                    at which point it will step back to the previous recursive call
                    and continue to work through that"""
                    if v == a and k not in self.dfs_path:
                        start = k  # set the start node to the first connection
                        g.dfs(graph, start)  # calls itself with new start node
        return self.dfs_path

    def bfs(self, graph, start):
        s = sorted(self.edge_location.items())
        a = -1  # to keep track of location in the list
        if start in self.queue:  # removes start from queue
            self.queue.remove(start)
        if start not in self.bfs_path:  # adds start to path
            self.bfs_path.append(start)
        """iterates through all possible connections adding them to the queue
        and to the path"""
        for i in self.edge[self.edge_location[start]]:
            a += 1
            if i != 0:
                for k, v in s:  # k = key, v = value
                    if v == a and k not in self.bfs_path:
                        self.queue.append(k)
                        self.bfs_path.append(k)
        """calls teh function with the first item in the queue until it is empty"""
        if len(self.queue) == 0:
            return self.bfs_path
        else:
            g.bfs(graph, self.queue[0])
        return self.bfs_path

if __name__ == '__main__':
    g = Graph()
    g.add_node(Node("A"))
    g.add_node(Node("B"))
    g.add_node(Node("C"))
    nodes = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    for _node in nodes:
        g.add_node(Node(_node))
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "E")
    g.add_edge("C", "E")
    g.add_edge("D", "E")
    g.add_edge("B", "D")
    g.add_edge("D", "F")
    g.add_edge("F", "G")
    g.add_edge("G", "I")
    g.add_edge("D", "H")
    g.add_edge("H", "J")
    g.add_edge("L", "K")
    g.add_edge("J", "L")
    g.add_edge("L", "N")
    g.add_edge("M", "N")
    g.add_edge("E", "M")
    g.add_edge("G", "N")
    g.display_graph()
    file_1 = open("Depth_First.txt", 'w')
    file_1.write(str(g.dfs(g, input("pick a node in the graph: "))))
    file_1.close()
    file_2 = open("Breadth_First.txt", "w")
    file_2.write(str(g.bfs(g, input("pick a node in the graph: "))))
    file_2.close()
