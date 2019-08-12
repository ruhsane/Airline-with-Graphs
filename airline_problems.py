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

    '''
    First problem : see if we can travel with each flight once and come back to the original city
    call method is_eulerian()
    '''
    problem1 = g.is_eulerian()
    if problem1 == True:
        print("This graph has eulerian cycle, meaning there is a way we can take every possible flight route exactly once and end up at the original airport where we started the trip.")
    else:
        print("There is no eulerian cycle. There is no way we can take every possible flight route exactly once and end up at the original airport where we started the trip.")


    '''
    2nd problem: find shortest path from airport A to airport B
    '''
    airport_A = "SIN"
    airport_B = "AUH"
    problem2 = g.breadth_first_search(airport_A, airport_B)
    print("The shortest path from %s to %s is: %s" % (airport_A, airport_B, problem2))


    '''
    3rd problem: find a airport that has the most amount of connected flights
    '''
    print("The airport that has the most amount of connected flights is: ")
    print(g.maximum_degree())