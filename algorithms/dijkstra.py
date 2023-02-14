class Graph:
    def __init__(self):
        self.graph = dict()
    
    def add_edge(self, node1, node2, weight):
        if node1 in self.graph:
            self.graph[node1][node2] = weight
            if node2 in self.graph:
                self.graph[node2][node1] = weight
            else:
                self.graph[node2] = {node1: weight}
        else:
            self.graph[node1] = {node2: weight}
            self.graph[node2] = {node1: weight}
    
    def all_visited(self, visited) -> bool:
        for x in visited:
            if visited[x]['visited'] == False:
                return False
        return True

    def ver_smallest_distance(self, visited):
        min = 999999999
        for x in visited:
            if visited[x]['total_distance'] < min and visited[x]['visited'] == False:
                min = visited[x]['total_distance']

        for x in visited:
            if visited[x]['total_distance'] == min and visited[x]['visited'] == False:
                return x

    def dijkstra(self, ver):
        visited = dict() # make a dict to track visited v

        for x in self.graph: 
            visited[x] = {'visited': False, 'total_distance': 99999999} # some large arbitary value
        visited[ver].update({'visited': True, 'total_distance': 0}) # starting vertex

        while self.all_visited(visited) != True:
            for x in self.graph[ver]:
                if visited[x]['total_distance'] > visited[ver]['total_distance'] + self.graph[ver][x]:
                    visited[x]['total_distance'] = visited[ver]['total_distance'] + self.graph[ver][x]
            visited[ver]['visited'] = True
            ver = self.ver_smallest_distance(visited)

        for x in visited:
            print(x, " path: ", visited[x]['total_distance'])

g = Graph()

g.add_edge('A', 'B', 1.3)
g.add_edge('A', 'E', 4)
g.add_edge('A', 'H', 0.5)

g.add_edge('B', 'E', 1.2)
g.add_edge('B', 'D', 2.4)
g.add_edge('B', 'C', 0.7)

g.add_edge('C', 'D', 0.4)
g.add_edge('C', 'F', 3)

g.add_edge('D', 'E', 0.1)
g.add_edge('D', 'H', 2.3)
g.add_edge('D', 'G', 1)

g.add_edge('E', 'H', 1.3)

g.add_edge('F', 'G', 0.7)
g.add_edge('F', 'J', 2.1)

g.add_edge('G', 'H', 1)
g.add_edge('G', 'J', 4.9)

print(g.graph)

g.dijkstra('A')
