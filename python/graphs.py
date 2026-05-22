class Vertex: #Represents a Node/Vertex in the Graph - uses an Adjacency List representation for the Graph
    def __init__(self, key):
        self.key = key
        self.adjacents: list[Vertex] = []

class Graph:
    def __init__(self):
        self.graph:list[Vertex] = []

    def add_vertex(self, key, edges: list|None):
        """
        @Param -> key - The key/value at the Vertex
        @Param -> edges - The Nodes/Vertices that form connection with the key Vertex
        """
        index_map = {vertex.key: i for i, vertex in enumerate(self.graph)}

        if key in index_map:
            _vertex = self.graph[index_map[key]]
            self._add_helper(_vertex, index_map, edges)
        else:
            new_vertex = Vertex(key)
            self._add_helper(new_vertex, index_map, edges)
            self.graph.append(new_vertex)
    
    def _add_helper(self, vertex: Vertex, index_map: dict, edges):
        if edges:
            for node in edges:
                if node in index_map:
                    vertex.adjacents.append(self.graph[index_map[node]])
                else:
                    vertex.adjacents.append(Vertex(node))
                    self.graph.append(vertex.adjacents[-1])
    
    def BFS(self):
        import random
        visited = set()
        traversal_order = []
        starting_vertex = random.choice(self.graph)
        print(starting_vertex.key)

        from python.queues import Simple_Queue
        _bfs_queue = Simple_Queue()
        _bfs_queue.enqueue(starting_vertex)

        self._BFS_helper(_bfs_queue, visited, traversal_order)
        return traversal_order

    from python.queues import Simple_Queue
    def _BFS_helper(self, bfs_queue: Simple_Queue, visited: set, traversal_order: list):
        if bfs_queue.is_empty():
            return
        
        current_vertex: Vertex = bfs_queue.dequeue()
        visited.add(current_vertex)
        traversal_order.append(current_vertex.key)
        bfs_queue.enqueue([vertex for vertex in current_vertex.adjacents if vertex not in bfs_queue.queue and vertex not in visited])
        return self._BFS_helper(bfs_queue, visited, traversal_order)
    
    def DFS(self):
        import random
        visited = set()
        traversal_order = []
        starting_vertex = random.choice(self.graph)
        print(starting_vertex.key)

        from python.stack import Stack
        _dfs_stack = Stack(len(self.graph))
        _dfs_stack.push(starting_vertex)

        self._DFS_helper(_dfs_stack, visited, traversal_order)
        return traversal_order

    from python.stack import Stack    
    def _DFS_helper(self, dfs_stack: Stack, visited: set, traversal_order: list):
        import random
        top: Vertex = dfs_stack.peek()
        if not top:
            return
        elif top.adjacents:
            remaining_adjacents = set(top.adjacents) - (set(dfs_stack.stack) | visited)
            if remaining_adjacents:
                _next_vertex = random.choice(list(remaining_adjacents))
                # print(_next_vertex.key)
                dfs_stack.push(_next_vertex)
            else:
                visited.add(dfs_stack.pop())
                traversal_order.append(top.key)
            return self._DFS_helper(dfs_stack, visited, traversal_order)
        else:
            popped_vertex = dfs_stack.pop()
            traversal_order.append(popped_vertex.key)
            visited.add(popped_vertex)
            return self._DFS_helper(dfs_stack, visited, traversal_order)
        
#Adjacency Matrix Representation for Graph
class MatrixGraph:
    def __init__(self):
        self.keys = []
        self.key_to_index = {}
        self.matrix = []

    def add_vertex(self, key):
        if key in self.key_to_index:
            return

        self.key_to_index[key] = len(self.keys)
        self.keys.append(key)

        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * len(self.keys))

    def add_edge(self, u, v, weight=1, undirected=True):
        i = self.key_to_index[u]
        j = self.key_to_index[v]
        self.matrix[i][j] = weight
        if undirected:
            self.matrix[j][i] = weight


#Example Usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(1, [4, 2])
    graph.add_vertex(4, [1, 3])
    graph.add_vertex(2, [1, 3, 8, 7, 5])
    graph.add_vertex(3, [2, 4, 10, 9])
    graph.add_vertex(8, [2, 7, 5])
    graph.add_vertex(7, [2, 8, 5])
    graph.add_vertex(5, [2, 7, 8, 6])
    graph.add_vertex(10, [3])
    graph.add_vertex(9, [3])
    graph.add_vertex(6, [5])

    graph2 = MatrixGraph()
    graph2.add_vertex(1)
    graph2.add_vertex(5)
    graph2.add_vertex(7)
    graph2.add_vertex(9)
    graph2.add_vertex(4)
    graph2.add_vertex(3)
    graph2.add_vertex(8)
    graph2.add_vertex(10)
    graph2.add_vertex(6)
    graph2.add_vertex(2)

    graph2.add_edge(1, 5)
    graph2.add_edge(1, 7)
    graph2.add_edge(1, 6)
    graph2.add_edge(5, 9)
    graph2.add_edge(5, 4)
    graph2.add_edge(7, 9)
    graph2.add_edge(7, 3)
    graph2.add_edge(9, 2)
    graph2.add_edge(4, 2)
    graph2.add_edge(3, 8)

    graph2.add_vertex(8)
    graph2.add_vertex(10)
    graph2.add_vertex(6)
    graph2.add_vertex(2)

    graph2.add_edge(8, 3)
    graph2.add_edge(10, 8)
    graph2.add_edge(6, 10)
    graph2.add_edge(2, 9)
    graph2.add_edge(2, 4)


    bfs_traversal = graph.BFS()
    dfs_traversal = graph.DFS()

    bfs_traversal2 = graph2.BFS()
    dfs_traversal2 = graph2.DFS()

    print("BFS Traversal:", bfs_traversal)
    print("DFS Traversal:", dfs_traversal)
    print("BFS Traversal 2:", bfs_traversal2)
    print("DFS Traversal 2:", dfs_traversal2)