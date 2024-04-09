from operator import iand
from functools import reduce

def minimumCost(n, edges, query):
    graph = make_graph(edges)
    output_cost = []
    node_to_cluster_id = {}
    cluster_id_to_weight = {}
    cluster_id = 0
    for q in query:
        start_node = q[0]
        end_node = q[1]
        if start_node == end_node:
            output_cost.append(0)
        elif start_node in node_to_cluster_id.keys() and end_node in node_to_cluster_id.keys() and node_to_cluster_id[start_node] == node_to_cluster_id[end_node]:
            output_cost.append(cluster_id_to_weight[node_to_cluster_id[start_node]])
        elif start_node in node_to_cluster_id.keys() or end_node in node_to_cluster_id.keys():
            output_cost.append(-1)
        elif start_node in graph.keys() and end_node in graph.keys():
            weight, visited_nodes = bfs(graph, start_node)
            cluster_id_to_weight[cluster_id] = weight
            for node in visited_nodes:
                node_to_cluster_id[node]=cluster_id
            if end_node in node_to_cluster_id.keys() and node_to_cluster_id[end_node] == cluster_id:
                output_cost.append(weight)
            else:
                output_cost.append(-1)
            cluster_id += 1
        else:
            output_cost.append(-1)
    return output_cost

def minimumCost_1(n, edges, query):
    graph = make_graph(edges)
    output_cost = []
    visited_nodes_list = []
    visited_weights_list = []
    for q in query:
        start_node = q[0]
        end_node = q[1]
        if start_node == end_node:
            output_cost.append(0)
        elif start_node in graph.keys() and end_node in graph.keys():
            flag = True
            for ind, visited_nodes_set in enumerate(visited_nodes_list):
                if start_node in visited_nodes_set and end_node in visited_nodes_set:
                    output_cost.append(reduce(iand,visited_weights_list[ind]))
                    flag = False
                    break
            if flag:
                weights, visited_nodes = bfs(graph, start_node)
                visited_nodes_list.append(set(visited_nodes))
                visited_weights_list.append(weights)
                if end_node in visited_nodes:
                    output_cost.append(reduce(iand,weights))
                else:
                    output_cost.append(-1)
        else:
            output_cost.append(-1)
    return output_cost

def minimumCost_0(n, edges, query):
    graph = make_graph(edges)
    output_cost = []
    for q in query:
        start_node = q[0]
        end_node = q[1]
        if start_node == end_node:
            output_cost.append(0)
        elif start_node in graph.keys() and end_node in graph.keys():
            weights, visited_nodes = bfs(graph, start_node)
            if end_node in visited_nodes:
                output_cost.append(reduce(iand,weights))
            else:
                output_cost.append(-1)
        else:
            output_cost.append(-1)
    return output_cost

def make_graph(edges):
    graph = {}
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        weight = edge[2]
        if start_node in graph.keys():
            graph[start_node].append([end_node, weight])
        else:
            graph[start_node] = [[end_node, weight]]
        
        if end_node in graph.keys():
            graph[end_node].append([start_node, weight])
        else:
            graph[end_node] = [[start_node, weight]]
    return graph


def bfs(graph, start_node):
    nodes_to_visit = []
    nodes_to_visit += graph[start_node]
    weights = []
    visited_nodes = [start_node]
    while len(nodes_to_visit)>0:
        node = nodes_to_visit.pop()
        if node[0] not in visited_nodes:
            nodes_to_visit += graph[node[0]]
            visited_nodes.append(node[0])
        weights.append(node[1])
    return(reduce(iand,weights), visited_nodes)



def test_0():
    n = 5; edges = [[0,1,7],[1,3,7],[1,2,1]]; query = [[0,3],[3,4]]
    assert minimumCost(n, edges, query) == [1,-1]

def test_1():
    n = 3; edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]; query = [[1,2]]
    assert minimumCost(n, edges, query) == [0]

def test_2():
    n = 9; edges = [[0,4,7],[3,5,1],[1,3,5],[1,5,1]]; query = [[0,4],[1,5],[3,0],[3,3],[3,2],[2,0],[7,7],[7,0]]
    assert minimumCost(n, edges, query) == [7,1,-1,0,-1,-1,0,-1]

if __name__ == '__main__':
    test_2()
    test_1()
    test_0()
     