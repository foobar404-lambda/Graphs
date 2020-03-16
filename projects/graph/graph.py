from util import Stack, Queue  # These may come in handy


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    #!MINE
    def dft_recursive(self, vertex, stack=None, history={}):
        if stack == None:
            stack = Stack()
        else:
            if vertex in history:
                return

            if stack.size == 0:
                return

        print(vertex)
        history[vertex] = True

        for neighbor in self.vertices[vertex]:
            if neighbor not in history:
                stack.push(neighbor)

        self.dft_recursive(stack.pop(), stack, history)

    def bfs(self, starting_vertex, destination_vertex):
        que = Queue()
        trigger = True
        node = starting_vertex
        history = {}

        while trigger:
            for neighbor in self.vertices[node]:
                que.add(node)

            node = que.dequeue()
            history[node] = True

            if node == destination_vertex:
                return

            if que.size == 0:
                trigger = False

        return None

    def dfs():
        pass

    def dfs_recursive():
        pass

