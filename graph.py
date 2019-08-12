""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""
from vertex import Vertex

class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.directed = False
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # increment the number of vertices
        self.numVertices += 1
        # create a new vertex
        vert = Vertex(key)
        # add the new vertex to the vertex list
        self.vertList[key] = vert
        # return the new vertex
        return vert

    def get_vertex(self, key):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key]

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        if f not in self.vertList:
        # add it
            self.add_vertex(f)
        if t not in self.vertList:
            self.add_vertex(t)

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        f_vert = self.get_vertex(f)
        t_vert = self.get_vertex(t)

        f_vert.add_neighbor(t_vert, cost)

        self.numEdges += 1


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def is_eulerian(self):
        '''
        returns boolean of whether or not the graph is eulerian
        A graph has an Eulerian cycle iff every vertex has even degree.
        '''
        for vert in self.vertList.values():
            degree = len(vert.get_neighbors())
            if degree % 2 != 0:
                print("this vertex has odd degree which makes impossible for eurelian: ", vert)
                return False
        return True

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())
