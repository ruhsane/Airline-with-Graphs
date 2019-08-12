from graph import Graph

def make_graph_from_file(text_file):
    '''
    reads file and make it into a graph object with respective properties.
    '''

    # Create the graph
    graph = Graph()

    # Opens and Parses through the text file to set up Graph
    with open(text_file, "r") as open_file:

        for line in open_file:

            clean_line = line.strip()

            # make an array of the connected edges with the weight, split by comma
            edge_list = line.strip("()\n").split(',')

            # first item in the list is the 'from' vertex airport
            from_v = edge_list[0]
            # second item in the list is the 'to' vertex airport
            to_v = edge_list[1]
            # third argument is the distance 
            distance = edge_list[2]

            # add edge from 'from' to 'to' with 'distance'
            graph.add_edge(from_v, to_v, distance)

            
        return graph

import argparse
if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    g = make_graph_from_file(args.filename)
    print(g)

    # Output the vertices & edges
    print("# Verticies:", g.numVertices, "\n")
    print("# Edges:", g.numEdges, "\n")

    print("Edge List:")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s , %s )" % (v.get_id(), w.get_id(), v.get_edge_weight(w)))