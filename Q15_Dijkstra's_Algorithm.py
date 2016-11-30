class Node:
    def __init__(self, value):
        self.vertex = value


class Graph(object):
    def __init__(self):
        self.edge = []  # list of lists of each nodes possible edges
        self.edge_location = {}  # dictionary of the position of the node within the above dictionary

    def add_vertex(self, x):
        for _list in self.edge:
            _list.append(0)
        self.edge.append([0] * (len(self.edge) + 1))
        self.edge_location[x.vertex] = len(self.edge_location)

        """self.edge[self.edge_location[x,y]] will find the list to be
        updated and [self.edge_location[y,x]] will point to the correct value
        in the list to be updated"""
    def add_edge(self, x, y, weight):
        self.edge[self.edge_location[x]][self.edge_location[y]] = weight
        self.edge[self.edge_location[y]][self.edge_location[x]] = weight

    def dijkstra(self, start, destination):
        s = start
        dist = {}  # dict of the distance to each node from the start node
        prev = {}  # dict of which node each node connects to in its shortest path
        dist_1 = {}  # dict which is the same as dist but can be used for future iteration
        q = sorted(self.edge_location.keys())  # needed as base case
        for i, j in self.edge_location.items():
            dist[i] = 999  # set all distances to 999(infinity)
            dist_1[i] = 999
            prev[i] = "unknown"  # set all previous nodes to "unknown"
        dist[start] = 0     # set start node distance to 0
        dist_1[start] = 0
        while len(q) != 0:
            current_shortest_path = min(dist_1.values())  #
            for node, distance in dist_1.items():
                if distance == current_shortest_path:   # finds node with shortest path
                    w = node
                    q.remove(node)      # removes from q and dist_1 as no shorter path can be found for this node
                    del(dist_1[node])
                    break       # stops iterating
            b = self.edge[self.edge_location[w]]  # b becomes the list of all possible connections to the current node
            a = -1  # to keep track of what position in b the current iteration is on
            for con in b:  # checks each possible connection to b
                a += 1
                if con != 0:  # when one is found
                    alt = dist[w] + con  # an alternate path is calculated to the connect node
                    if alt < dist[sorted(self.edge_location)[a]]:  # if it is less than the current path
                        z = sorted(self.edge_location)
                        prev[z[a]] = w  # set its previous node connection to node with current shortest path
                        start = z[a]  # new start node becomes the node just added to the path
                        dist_1[start] = alt  # distance updated with the alternate distance
                        dist[start] = alt
        shortest_path(prev, s, destination)
        print("Total distance =", dist[destination])


def shortest_path(prev, start, destination):
    path = [destination]  # list created to find the path
    while path[len(path) - 1] != start:  # loops until start node is reached
        for i, j in prev.items():  # iterates through to find the destination and the previous node in the path
            if i == destination and j != start:  # when found
                if i not in path:   # checks if it is in path (because of destination)
                    path.append(i)  # adds each connection to the path
                destination = j
            elif i == destination and j == start:  # when start is the next previous node
                path.append(i)  # add both the node currently looking for
                path.append(start)  # and the start node to path
    path.reverse()  # reverse teh list to find path from start -> destination
    print("path =", path)


if __name__ == '__main__':
    g = Graph()
    g.add_vertex(Node("A"))
    g.add_vertex(Node("B"))
    g.add_vertex(Node("C"))
    nodes = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    for _node in nodes:
        g.add_vertex(Node(_node))
    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "E", 7)
    g.add_edge("C", "E", 6)
    g.add_edge("D", "E", 1)
    g.add_edge("B", "D", 6)
    g.add_edge("D", "F", 4)
    g.add_edge("F", "G", 2)
    g.add_edge("G", "I", 3)
    g.add_edge("D", "H", 9)
    g.add_edge("H", "J", 2)
    g.add_edge("L", "K", 4)
    g.add_edge("J", "L", 3)
    g.add_edge("L", "N", 2)
    g.add_edge("M", "N", 1)
    g.add_edge("E", "M", 4)
    g.add_edge("G", "N", 3)
    g.dijkstra("A", "K")
