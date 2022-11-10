# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:26:42 2022

@author: DSL1PVI
"""

class MST:
    
    def __init__(self, node_list, dist_mat, edge_list, start_node_index = 2):
        self.node_list = node_list.copy()
        self.dist_mat = dist_mat.copy()
        self.edge_list = edge_list.copy()
        self.start_node_index = start_node_index
        self.MST_edges = []
        self.MST_distance = 0
        self.get_MST()
        self.plot_MST_edges()
        
    def get_MST(self):
        self.counter = 1
        node_A = self.node_list[self.start_node_index]
        self.already_visited_nodes = [node_A]
        node_B = Route.get_closest_node(node_A, self.dist_mat, self.node_list, 
                                        self.already_visited_nodes)
        
        self.MST_distance += node_A.distance(node_B)
        self.MST_edges.append(Edge(self.counter,node_A, node_B))
        self.already_visited_nodes.append(node_B)
        self.explore_MST(node_A, node_B, self.already_visited_nodes)
        
    def explore_MST(self, node_A, node_B, already_visited_nodes):
        
        if len(already_visited_nodes) == len(self.node_list):
            return
        
        node_sA = Route.get_closest_node(node_A, self.dist_mat, self.node_list, 
                                        self.already_visited_nodes)
        
        node_sB = Route.get_closest_node(node_B, self.dist_mat, self.node_list, 
                                        self.already_visited_nodes)
        
        if node_A.distance(node_sA) <= node_B.distance(node_sB):
            self.MST_distance += node_A.distance(node_sA)
            self.counter += 1
            self.MST_edges.append(Edge(self.counter,node_A, node_sA))
            self.already_visited_nodes.append(node_sA)
            node_A = node_sA
        else:
            self.MST_distance += node_B.distance(node_sB)
            self.counter += 1
            self.MST_edges.append(Edge(self.counter,node_B, node_sB))
            self.already_visited_nodes.append(node_sB)
            node_B = node_sB
            
        self.explore_MST(node_A, node_B, self.already_visited_nodes)
        
    def plot_MST_edges(self):
        for edge in self.MST_edges:
            x_values = [edge.node1.x, edge.node2.x]
            y_values = [edge.node1.y, edge.node2.y]
            plt.plot(x_values, y_values)
        plt.show()