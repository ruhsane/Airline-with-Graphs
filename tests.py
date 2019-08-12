import unittest

from graph import Graph
from vertex import Vertex

class VertexTest(unittest.TestCase):
    def test_init(self):
        # Tests the initialization of the Vertex class 
        v1 = "a"
        vertex = Vertex(v1)

        self.assertEqual(vertex.id, "a")
        self.assertDictEqual(vertex.neighbors, {})

    def test_add_neighbor(self):
        v1 = "a"
        vertex = Vertex(v1)

        vertex.add_neighbor("b", 0)
        self.assertTrue(any(vertex.neighbors))
        self.assertDictEqual(vertex.neighbors, {"b":0})

class GraphTest(unittest.TestCase):
    def test_init(self):
        # Tests the initialization of the Graph class
        graph = Graph()
        self.assertDictEqual(graph.vertList, {})
        self.assertEqual(graph.numVertices, 0)
        self.assertEqual(graph.numEdges, 0)

    def test_add_vertex(self):
        graph = Graph()

        # Creates test Verticies
        v1,v2,v3 = Vertex("a"), Vertex("b"), Vertex("c")

        # Add vertex "a"
        graph.add_vertex(v1)
        self.assertEqual(graph.numVertices, 1)
        self.assertEqual(graph.numEdges, 0)

        # Add vertex "b"
        graph.add_vertex(v2)
        self.assertEqual(graph.numVertices, 2)
        self.assertEqual(graph.numEdges, 0)

        # Add vertex "c"
        graph.add_vertex(v3)
        self.assertEqual(graph.numVertices, 3)
        self.assertEqual(graph.numEdges, 0)

    def test_add_edge(self):
        graph = Graph()

        # Create test Verticies
        v1,v2,v3 = Vertex("a"), Vertex("b"), Vertex("c")

        # Add verticies
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        self.assertEqual(graph.numVertices, 3)
        self.assertEqual(graph.numEdges, 0)

        # Create edges
        edges = [
            ("a", "b", 10),
            ("b", "c", 10),
            ("c", "a", 4)
        ]

        # Iterate through edges
        for edge in edges:
            fromVert, toVert, weight = edge
            graph.add_edge(fromVert, toVert, weight)

        self.assertEqual(graph.numEdges, 3)

    def text_get_verticies(self):
        graph = Graph()

        # Create test Verticies
        v1,v2,v3 = Vertex("a"), Vertex("b"), Vertex("c")

        # Add verticies
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        self.assertListEqual(graph.get_vertices, ["a","b","c"])


    def test_get_edges(self):
        graph = Graph()

        # Create test Verticies
        v1,v2,v3 = Vertex("a"), Vertex("b"), Vertex("c")

        # Add verticies
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        self.assertEqual(graph.numVertices, 3)
        self.assertEqual(graph.numEdges, 0)

        # Create edges
        edges = [
            ("a", "b", 10),
            ("b", "c", 10),
            ("c", "a", 4)
        ]

        # Iterate through edges
        for edge in edges:
            fromVert, toVert, weight = edge
            graph.add_edge(fromVert, toVert, weight)

        self.assertEqual(graph.numEdges, 3)

    def test_is_eulerian(self):
        graph = Graph()

        # Create test Verticies
        v1,v2,v3 = Vertex("a"), Vertex("b"), Vertex("c")
        # Add verticies
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        # Create edges
        edges = [
            ("a", "b", 10),
            ("b", "c", 10),
            ("c", "a", 4),
            ("c", "b", 2)
        ]
        # Add edges
        for edge in edges:
            fromVert, toVert, weight = edge
            graph.add_edge(fromVert, toVert, weight)

        self.assertFalse(graph.is_eulerian())

        graph2 = Graph()
        # Create test Verticies
        ve1,ve2,ve3 = Vertex("a"), Vertex("b"), Vertex("c")
        # Add verticies
        graph2.add_vertex(ve1)
        graph2.add_vertex(ve2)
        graph2.add_vertex(ve3)

        # Create edges
        edges = [
            ("a", "b", 10),
            ("a", "c", 10),
            ("b", "c", 10),
            ("b", "a", 2),
            ("c", "a", 4),
            ("c", "b", 2)
        ]
        # Add edges
        for edge in edges:
            fromVert, toVert, weight = edge
            graph2.add_edge(fromVert, toVert, weight)

        self.assertTrue(graph2.is_eulerian())