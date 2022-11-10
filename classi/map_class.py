# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:46:01 2022

@author: DSL1PVI
"""
import numpy as np
import matplotlib.pyplot as plt
import math   
import itertools
import pylab

from classi.route_class import RouteNN

rng = np.random.default_rng()
rng = np.random.default_rng(seed = 12345)
np.random.seed(10)


class Node:
    
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.num}, x:{self.x}, y:{self.y}"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
    
        

class Edge:
    
    def __init__ (self, num, node1, node2):
        self.num = num
        self.node1 = node1
        self.node2 = node2
        self.edge_len = node1.distance(node2)
        
    def __str__(self):
        return f"{self.num}, 1:{self.point1}, 2:{self.point2}, edge_len = {self.edge_len}"
    
    def __gt__(self,other):
        return self.edge_len > other.edge_len
    
    def __contains__(self, node):
        if node == self.node1 or node == self.node2:
            return True
        return False
    
    def nodes_inside_edge(self, node1, node2):
        if node1 == self.node1 and node2 == self.node2:
            return True
        elif  node1 == self.node2 and node2 == self.node1:
            return True
        else:
            return False
    



# class RouteNN:
    
#     def __init__(self, start_node, dist_mat, node_list):
#         self.start_node = start_node
#         self.temp_dist_mat = dist_mat.copy()
#         self.node_list = node_list
#         self.route_distance = self.nearest_neighbour()
        
         
#     def __str__(self):
#         return (f"start_node: {self.start_node}, distance = {self.route_distance}")
    
#     def __gt__(self, other):
#         return self.route_distance > other.route_distance
             
#     def nearest_neighbour(self):
#         nodi_visitati = 1
#         distance = 0
#         avoid_visit_nodes = [self.start_node]
#         self.route = [self.start_node]
        
#         while nodi_visitati < len(self.node_list):
             
#              end_node = RouteNN.get_closest_node(self.start_node, self.temp_dist_mat,
#                                                self.node_list, avoid_visit_nodes) 
#              self.route.append(end_node)
#              avoid_visit_nodes.append(end_node)
#              distance +=  self.start_node.distance(end_node)
#              self.start_node = end_node
#              nodi_visitati += 1
             
#         return distance
    
#     @staticmethod
#     def get_closest_node(start_node, dist_mat, node_list, avoid_visit_nodes):
        
#         for node in avoid_visit_nodes:
#             dist_mat[:,node.num] = 0
            
#         row_num = start_node.num
#         row = dist_mat[row_num,:]
        
#         minval = np.min(row[np.nonzero(row)])
#         min_index = np.where(row == minval)[0][0]
        
#         end_node = node_list[min_index]
#         return end_node
        
             
#     def plot_routes(self):
#         for i in range(1, len(self.route)):
#             x_values = [self.route[i-1].x, self.route[i].x]
#             y_values = [self.route[i-1].y, self.route[i].y]
            
#             plt.plot(x_values, y_values)
#         plt.show()
     
        
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
            
            

class Map:
    
    def __init__(self, map_name, num_points, max_x, max_y):
        self.map_name = map_name
        self.num_points = num_points
        self.map_max_x = max_x
        self.map_max_y = max_y
        self.node_list = []
        
    
    def __len__(self):
        return len(self.node_list)
    
    def __str__(self):
        return f"{self.map_name}, {self.num_points}"
        
    def generate_grid_random(self):
        x_values = rng.integers(low=0, high=self.map_max_x, size=self.num_points)
        y_values = rng.integers(low=0, high=self.map_max_y, size=self.num_points)
        self.grid = np.column_stack((x_values, y_values))
        
    def plot_grid(self):
        fig=plt.figure(1)
        ax=fig.add_axes([0,0,1,1])
        ax.scatter(self.grid[:,0], self.grid[:,1], color='r')
        plt.show()
        
    def generate_nodes(self):
        x_values = self.grid[:,0]
        y_values = self.grid[:,1]
        for i in range(self.num_points):
            self.node_list.append(Node(i, x_values[i], y_values[i] ))
            
    def generate_edges(self):
        self.couples_nodes = list(itertools.combinations(self.node_list, 2))
        self.edge_list = [Edge(i, couple[0], couple[1]) for i, couple in enumerate(self.couples_nodes)]
        
    def plot_edges(self):
        for edge in self.edge_list:
            x_values = [edge.node1.x, edge.node2.x]
            y_values = [edge.node1.y, edge.node2.y]
            plt.plot(x_values, y_values)
        plt.show()
        
    def create_distance_matrix(self):
        self.dist_mat = np.zeros((self.num_points, self.num_points))
        for i, node_start in enumerate(self.node_list):
            for j, node_end in enumerate(self.node_list[i:], start = i):
                if i != j:
                    self.dist_mat[i,j] = node_start.distance(node_end)
        
        self.dist_mat =  self.dist_mat + np.transpose(self.dist_mat)
          
    def closest_neighbour(self, start_node):
        self.route_CN = RouteNN(self.dist_mat, self.node_list, self.edge_list, start_node) 
        self.NN_distance = self.route_CN.route_distance  
        self.route_CN.plot_routes()
        
        
    # def generate_MST(self):
    #     self.mst = MST(self.node_list, self.dist_mat, self.edge_list, start_node_index = 3)
        
        
    
    
if __name__ == "__main__":
    
    mappa1 = Map('mappa1', 6, 50, 50)
    mappa1.generate_grid_random()
    mappa1.plot_grid()
    mappa1.generate_nodes()
    mappa1.generate_edges()
    mappa1.plot_edges()
    mappa1.create_distance_matrix()
    mappa1.closest_neighbour(mappa1.node_list[3])
    mappa1.generate_MST()
    


