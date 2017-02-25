from fractions import gcd

def answer(banana_list):
    banana_graph = getgraph(banana_list)
    return getminguards(banana_graph)

def getminguards(graph):
    total = 0
    while len(graph) > 0:
        graph = sorted(graph, key = len)
        while len(graph[0]) == 0 and len(graph) > 0:
            total += 1
            graph = remove(graph, 0)
        currentlen = len(graph[0])
        while len(graph[0]) == currentlen and len(graph) > 0:
            graph = remove_pair(graph, 0, graph[0][0])


def getgraph(ls):
    graph = []
    for i in range(0, len(ls)):
        graph.append([])
        for j in range(0, len(ls)):
            if (i != j):
                if (infloop(ls[i], ls[j])):
                    graph[i].append(j)
    return graph

def remove(graph, idx):
    #removes a node that has no edges
    del graph[idx]
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            graph[i][j] -= 1
    return graph

def remove_pair(graph, idx1, idx2):
    #removes a pair of nodes and all edges connected to them
    if idx1 < idx2:
        idx1, idx2 = idx2, idx1
    

def infloop(a, b):
    ratio_sum = (a + b) / gcd(a, b)
    if (ratio_sum & (ratio_sum - 1)) == 0:
        return False
    return True
    
    
