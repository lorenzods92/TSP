# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:26:42 2022

@author: DSL1PVI
"""

from classi.map_class import Node, Edge



    
def creates_a_cycle(edge, greedy_edges):
        temp_greedy_edges = greedy_edges.copy()
        # temp_greedy_edges.append(edge)
        start = edge.node1
        end = edge.node2
        
        return depthFirstTraversal(start, end, temp_greedy_edges)
    
def depthFirstTraversal(start, end,  temp_greedy_edges):
    graph = create_graph(temp_greedy_edges)
    if not graph:
        return False
    stack = [start]
    visited = []
    while stack:
        current = stack.pop(-1)
        visited.append(current)
        print(current)
        if current not in graph:
            return False
        for elem in graph[current]:
            if elem not in visited:
                stack.append(elem)
            if elem == end:
                return True
    return False

def create_graph(edges):
        graph = {}
        
        for edge in edges:
            if edge.node1 not in graph:
                graph[edge.node1] = []
            if edge.node2 not in graph:
                graph[edge.node2] = []
            
            graph[edge.node1].append(edge.node2)
            graph[edge.node2].append(edge.node1)
        print(graph)
        return graph

node0 = Node(0, 2, 2)
node1 = Node(1, 2, 0)
node2 = Node(2, 0, 0)
node3 = Node(3, 0, 2)
node4 = Node(4, 1, 3)
node6 = Node(6, 5, 3)

edge0 = Edge(0, node0, node1)
edge1 = Edge(1, node1, node2)
edge2 = Edge(2, node2, node3)
edge3 = Edge(3, node3, node0)
edge4 = Edge(4, node3, node4)
edge5 = Edge(5, node1, node6)
edge6 = Edge(6, node6, node4)

edges = [edge0, edge1, edge2, edge4, edge5]
edges = [edge3, edge0, edge1, edge2, edge4, edge5]

print(creates_a_cycle(edge6, edges))







 
