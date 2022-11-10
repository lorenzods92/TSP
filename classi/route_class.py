# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:19:26 2022

@author: DSL1PVI
"""
import numpy as np
import matplotlib.pyplot as plt
import math   
import itertools



class Route:
    
    def __init__(self, dist_mat, node_list, edge_list, start_node):
        self.dist_mat = dist_mat.copy()
        self.node_list = node_list
        self.edge_list = edge_list
        self.start_node = start_node
        


class RouteNN(Route):
    
    def __init__(self, dist_mat, node_list, edge_list, start_node):
        super().__init__(dist_mat, node_list, edge_list, start_node)
        
        self.route_distance = self.nearest_neighbour()
        
         
    def __str__(self):
        return (f"start_node: {self.start_node}, distance = {self.route_distance}")
    
    def __gt__(self, other):
        return self.route_distance > other.route_distance
             
    def nearest_neighbour(self):
        nodi_visitati = 1
        distance = 0
        avoid_visit_nodes = [self.start_node]
        self.route = [self.start_node]
        
        while nodi_visitati < len(self.node_list):
             
              end_node = RouteNN.get_closest_node(self.start_node, self.dist_mat,
                                                self.node_list, avoid_visit_nodes) 
              self.route.append(end_node)
              avoid_visit_nodes.append(end_node)
              distance +=  self.start_node.distance(end_node)
              self.start_node = end_node
              nodi_visitati += 1
             
        return distance
    
    @staticmethod
    def get_closest_node(start_node, dist_mat, node_list, avoid_visit_nodes):
        
        for node in avoid_visit_nodes:
            dist_mat[:,node.num] = 0
            
        row_num = start_node.num
        row = dist_mat[row_num,:]
        
        minval = np.min(row[np.nonzero(row)])
        min_index = np.where(row == minval)[0][0]
        
        end_node = node_list[min_index]
        return end_node
        
             
    def plot_routes(self):
        for i in range(1, len(self.route)):
            x_values = [self.route[i-1].x, self.route[i].x]
            y_values = [self.route[i-1].y, self.route[i].y]
            
            plt.plot(x_values, y_values)
        plt.show()
     
        
# class MST:
    
#     def __init__(self, node_list, dist_mat, edge_list, start_node_index = 2):
#         self.node_list = node_list.copy()
#         self.dist_mat = dist_mat.copy()
#         self.edge_list = edge_list.copy()
#         self.start_node_index = start_node_index
#         self.MST_edges = []
#         self.MST_distance = 0
#         self.get_MST()
#         self.plot_MST_edges()
        
#     def get_MST(self):
#         self.counter = 1
#         node_A = self.node_list[self.start_node_index]
#         self.already_visited_nodes = [node_A]
#         node_B = Route.get_closest_node(node_A, self.dist_mat, self.node_list, 
#                                         self.already_visited_nodes)
        
#         self.MST_distance += node_A.distance(node_B)
#         self.MST_edges.append(Edge(self.counter,node_A, node_B))
#         self.already_visited_nodes.append(node_B)
#         self.explore_MST(node_A, node_B, self.already_visited_nodes)
        
#     def explore_MST(self, node_A, node_B, already_visited_nodes):
        
#         if len(already_visited_nodes) == len(self.node_list):
#             return
        
#         node_sA = Route.get_closest_node(node_A, self.dist_mat, self.node_list, 
#                                         self.already_visited_nodes)
        
#         node_sB = Route.get_closest_node(node_B, self.dist_mat, self.node_list, 
#                                         self.already_visited_nodes)
        
#         if node_A.distance(node_sA) <= node_B.distance(node_sB):
#             self.MST_distance += node_A.distance(node_sA)
#             self.counter += 1
#             self.MST_edges.append(Edge(self.counter,node_A, node_sA))
#             self.already_visited_nodes.append(node_sA)
#             node_A = node_sA
#         else:
#             self.MST_distance += node_B.distance(node_sB)
#             self.counter += 1
#             self.MST_edges.append(Edge(self.counter,node_B, node_sB))
#             self.already_visited_nodes.append(node_sB)
#             node_B = node_sB
            
#         self.explore_MST(node_A, node_B, self.already_visited_nodes)
        
#     def plot_MST_edges(self):
#         for edge in self.MST_edges:
#             x_values = [edge.node1.x, edge.node2.x]
#             y_values = [edge.node1.y, edge.node2.y]
#             plt.plot(x_values, y_values)
#         plt.show()