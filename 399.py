def makeGraph(equations, values):
    graph ={}
    for ind, equation in enumerate(equations):
        start_node = equation[0]
        end_node = equation[1]
        try:
            graph[start_node].append([end_node,values[ind]])
        except KeyError:
            graph[start_node] = [[end_node,values[ind]]]
        
        try:
            graph[end_node].append([start_node,1/values[ind]])
        except KeyError:
            graph[end_node] = [[start_node,1/values[ind]]]
    return graph

def findNode(graph, start_node, end_node):

    visited_parents = []
    
    visited_nodes = {}
    if start_node not in graph.keys():
        return -1
    if end_node not in graph.keys():
        return -1
    if start_node == end_node:
        return 1

    visited_nodes[start_node] = 1

    candidates = [start_node]
    while len(candidates)>0:
        parent = candidates.pop()
        if parent not in visited_parents:
            visited_parents.append(parent)
            for new_neighbor in graph[parent]:
                if new_neighbor[0] == end_node:
                    return visited_nodes[parent]*new_neighbor[1]
                else:
                    candidates.append(new_neighbor[0])
                    visited_nodes[new_neighbor[0]] = visited_nodes[parent]*new_neighbor[1]

    return -1


def calcEquation(equations, values, queries):
    graph = makeGraph(equations, values)
    results = []
    for query in queries:
        start_node = query[0]
        end_node = query[1]
        solution = findNode(graph, start_node, end_node)
        results.append(solution)
    return results




def test_0():
    equations = [["a","b"],["b","c"]]; values = [2.0,3.0]; queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    assert calcEquation(equations, values, queries) == [6.00000,0.50000,-1.00000,1.00000,-1.00000]

def test_1():
    equations = [["a","b"],["b","c"],["bc","cd"]]; values = [1.5,2.5,5.0]; queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    assert calcEquation(equations, values, queries) == [3.75000,0.40000,5.00000,0.20000]

def test_2():
    equations = [["a","b"]]; values = [0.5]; queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    assert calcEquation(equations, values, queries) == [0.50000,2.00000,-1.00000,-1.00000]

if __name__ == "__main__":
    test_0()
    test_1()
    test_2()