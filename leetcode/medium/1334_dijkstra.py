"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""

from collections import defaultdict


class Heap:

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    @staticmethod
    def newMinHeapNode(v, dist):
        return [v, dist]

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if (left < self.size and
                self.array[left][1]
                < self.array[smallest][1]):
            smallest = left

        if (right < self.size and
                self.array[right][1]
                < self.array[smallest][1]):
            smallest = right

        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    # Standard function to extract minimum
    # node from heap
    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty():
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        last_node = self.array[self.size - 1]
        self.array[0] = last_node

        # Update position of last node
        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not heapify. This is a O(Log n) loop
        while (i > 0 and self.array[i][1] <
               self.array[(i - 1) // 2][1]):
            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            # move to parent index
            i = (i - 1) // 2

    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(dist, n):
    # print ("Vertex\tDistance from source")
    for i in range(n + len(dist)):
        pass  # print ("%d\t\t%d" % (i,dist[i]))


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):

        # Add an edge from src to dest. A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        new_node = [dest, weight]
        self.graph[src].insert(0, new_node)

        # Since graph is undirected, add an edge
        # from dest to src also
        new_node = [src, weight]
        self.graph[dest].insert(0, new_node)

    # The main function that calculates distances
    # of the shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src):

        _V = self.V  # Get the number of vertices in graph
        dist = []  # dist values used to pick minimum
        # weight edge in cut

        # minHeap represents set E
        min_heap = Heap()

        # Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(_V):
            dist.append(1e7)
            min_heap.array.append(min_heap.
                                  newMinHeapNode(v, dist[v]))
            min_heap.pos.append(v)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        min_heap.pos[src] = src
        dist[src] = 0
        min_heap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        min_heap.size = _V

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while not min_heap.isEmpty():

            # Extract the vertex
            # with minimum distance value
            new_heap_node = min_heap.extractMin()
            u = new_heap_node[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (min_heap.isInMinHeap(v) and
                        dist[u] != 1e7 and pCrawl[1] + dist[u] < dist[v]):
                    dist[v] = pCrawl[1] + dist[u]

                    # update distance value
                    # in min heap also
                    min_heap.decreaseKey(v, dist[v])

        printArr(dist, _V)
        return dist


class Solution:
    @staticmethod
    def findTheCity(n: int, edges: [[int]], distanceThreshold: int) -> int:
        # Driver program to test the above functions
        graph = Graph(n)
        for edge in edges:
            graph.addEdge(edge[0], edge[1], edge[2])

        lowest = dict()
        for i in range(n):
            d = graph.dijkstra(i)
            # print(d)
            reach = []
            for j in range(n):
                if d[j] <= distanceThreshold:
                    reach.append(j)
            total = len(reach)
            lowest[total] = i
            # for di in d:
            #     if di[1] <= distanceThreshold:
            #         reach.append(di[0])
            # print(i, 'can reach', reach)
        # print(lowest)
        # dfs?
        return lowest[min(lowest.keys())]


assert Solution.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4) == 3
"""
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, 
but we have to return city 3 since it has the greatest number.
"""
assert Solution.findTheCity(n=5, edges=[[0, 1, 2],
                                        [0, 4, 8],
                                        [1, 2, 3],
                                        [1, 4, 2],
                                        [2, 3, 1],
                                        [3, 4, 1]], distanceThreshold=2) == 0
"""
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""
