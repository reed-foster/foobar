"""
Pairs of guards will bet bananas and thumb wrestle. The one with fewer bananas
will bet all of theirs, and the one with more matches the bet. The one with
more bananas always loses. Guards will enter an infinite loop if their banana
counts are never equal. Certain pairings will result in an infinite loop.

Write a function answer(banana_list) which, given a list of positive integers
representing the amount of bananas each guard starts with, returns the fewest
possible number of guards that will be left to watch the prisoners.

The length of banana_list will be between 1 and 100, and any guard can have
between 1 and 2 ^ 31 - 1 bananas

Examples:
>>> answer([1, 1])
2
>>> answer([1, 7, 3, 21, 19, 13])
0
"""

from fractions import gcd

class Graph:
    N = 0 #number of nodes
    nodes = [] #holds the value for each node
    connectednodes = [] #holds a list representing all the connected nodes for each node

    #holds the index representing the location of a node in a list of nodes sorted by degree
    #i.e. if sortednodes[0] = 3, then nodes[0] would be the 4th element of a list of nodes sorted by degree
    sortednodes = [] 
    
    def __init__(self, ls):
        self.N = len(ls)
        self.nodes = ls
        for i in range(0, len(ls)):
            self.connectednodes.append([])
            newlist = [] #holds values of all nodes connected to ls[i]
            for j in range(0, len(ls)):
                if (i != j):
                    if infloop(ls[i], ls[j]):
                        #ls[i] and ls[j] are connected iff they form an infinite loop
                        newlist.append(ls[j])
            self.connectednodes[i] = newlist
        self.sortednodes = self._getsortednodes()
    
    def _getsortednodes(self):
        #generate list of indicies of the graph's nodes after sorting them by degree
        sortedlist = sorted(self.nodes, key = self.degree)
        mapping = []
        for i in sortedlist:
            for j in range(0, self.nodes.count(i)):
                mapping.append(self.nodes.index(i) + j)
        return mapping
    
    def degree_by_idx(self, idx):
        return len(self.connectednodes[idx])
    
    def degree(self, nodeid):
        return len(self.connectednodes[self.nodes.index(nodeid)])

    def remove_node_by_idx(self, idx):
        self.N -= 1
        node = self.nodes.pop(idx)
        del self.connectednodes[idx]
        self.sortednodes = [i if i < idx else (i - 1 if i > idx else -1) for i in self.sortednodes]
        self.sortednodes.remove(-1)

        #remove all instances of node in other node's connectednodes lists
        for i in range(0, self.N):
            if node in self.connectednodes[i]:
                self.connectednodes[i].remove(node)
    
    def remove_node(self, nodeid):
        self.remove_node_by_idx(self.nodes.index(nodeid))

    def sort(self):
        self.sortednodes = self._getsortednodes()

def answer(banana_list):
    banana_graph = Graph(banana_list)
    return getminguards(banana_graph)

def getminguards(graph):
    total = 0
    while graph.N > 0:
        graph.sort()
        #remove all nodes with zero connections and increment the total number of free guards
        while graph.N > 0 and graph.degree_by_idx(graph.sortednodes[0]) == 0:
            total += 1
            graph.remove_node_by_idx(graph.sortednodes[0])
        if graph.N == 0:
            return total
        #remove a pair of nodes:
        #the first node and its first connected node
        node1 = graph.nodes[graph.sortednodes[0]]
        node2 = graph.connectednodes[graph.sortednodes[0]][0]
        graph.remove_node(node1)
        graph.remove_node(node2)
    return total

def infloop(a, b):
    # a and b enter an infinite loop iff
    # m + n is a power of two for m / n = a / b | m, n are relatively prime
    ratio_sum = (a + b) / gcd(a, b)
    if (ratio_sum & (ratio_sum - 1)) == 0:
        return False
    return True
    
    
