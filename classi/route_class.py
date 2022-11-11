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
     
        
    def __str__(self):
        start = self.start_node
        dist = self.route_distance
        return f"start node: {start}, distance: {dist}\n {self.route}"
    
    def __gt__(self, other):
        return self.route_distance > other.route_distance 
    
    def __getitem__(self, node_position):
        return self.route[node_position]
    
    def nearest_neighbour_route(self):
        already_visited_nodes = [self.start_node]
        route = [self.start_node]
        start_node = self.start_node
        
        while len(already_visited_nodes) < len(self.node_list):
             
              end_node = self.get_closest_node(start_node, already_visited_nodes) 
              route.append(end_node)
              already_visited_nodes.append(end_node)
              start_node = end_node 
             
        return route
    
    def get_closest_node(self, start_node, avoid_visit_nodes):
        for node in avoid_visit_nodes:
            self.dist_mat[:,node.num] = 0
            
        row_num = start_node.num
        row = self.dist_mat[row_num,:]
        
        minval = np.min(row[np.nonzero(row)])
        min_index = np.where(row == minval)[0][0]
        end_node = self.node_list[min_index]
        
        return end_node
    
    def get_route_distance(self):
        distance = 0
        for i in range(1, len(self.route)):
            distance += self.route[i-1].distance(self.route[i])
            
        return distance
        
    def plot_routes(self):
        for i in range(1, len(self.route)):
            x_values = [self.route[i-1].x, self.route[i].x]
            y_values = [self.route[i-1].y, self.route[i].y]
            
            plt.plot(x_values, y_values)
        plt.title('Nearest Neighbour')
        plt.show()
      
        
    def MST_tree(self):
        MST_nodes = []
        MST_edges = []
        available_edges = self.edge_list.copy()
        
        min_edge = min(available_edges)
        MST_nodes.extend([min_edge.node1, min_edge.node2])
        MST_edges.append(min_edge)
        available_edges.remove(min_edge)
        
        while len(MST_nodes) < len(self.node_list):
            min_edge = max(available_edges)
            
            for edge in available_edges:
                if edge.contains_exactly_one_node(MST_nodes) and edge.edge_len <= min_edge.edge_len:
                    min_edge_len = edge.edge_len
                    min_edge = edge
            
            MST_edges.append(min_edge)
            available_edges.remove(min_edge) 
            MST_nodes.extend([min_edge.node1, min_edge.node2])
            MST_nodes = list(set(MST_nodes))
        
        return MST_edges, MST_nodes
    
    
    def plot_MST(self):
        for edge in self.MST_edges:
            x_values = [edge.node1.x, edge.node2.x]
            y_values = [edge.node1.y, edge.node2.y]
            
            plt.plot(x_values, y_values)
        plt.title('MST')
        plt.show()
        
    
    def get_MST_distance(self):
        distance = 0
        for edge in self.MST_edges:
            distance += edge.edge_len
            
        return distance
            
       
        
            
    

class RouteNN(Route):
    
    def __init__(self, dist_mat, node_list, edge_list, start_node):
        super().__init__(dist_mat, node_list, edge_list, start_node)
        
        self.route = super().nearest_neighbour_route()
        self.route_distance = super().get_route_distance()
        self.MST_edges, self.MST_nodes = super().MST_tree()
        self.MST_distance = self.get_MST_distance()
        # super().plot_MST(self.MST_edges)
        
         

              
    
    
    
        
             
    
     
        
