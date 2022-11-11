# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:19:26 2022

@author: DSL1PVI
"""
import numpy as np
import matplotlib.pyplot as plt
import math   
import itertools
import queue
from collections import Counter



class Route:
    
    def __init__(self, dist_mat, node_list, edge_list):
        self.dist_mat = dist_mat.copy()
        self.node_list = node_list
        self.edge_list = edge_list

        
    def __str__(self):
        start = self.start_node
        dist = self.route_distance
        return f"start node: {start}, distance: {dist}\n {self.route}"
    
    def __gt__(self, other):
        return self.route_distance > other.route_distance 
    
    def __getitem__(self, node_position):
        return self.route[node_position]
    
    def nearest_neighbour_route(self, start_node):
        temp_dist_mat = self.dist_mat.copy()
        already_visited_nodes = [start_node]
        route = [start_node]
        
        while len(already_visited_nodes) < len(self.node_list):
             
              end_node = self.get_closest_node(start_node, already_visited_nodes, temp_dist_mat) 
              route.append(end_node)
              already_visited_nodes.append(end_node)
              start_node = end_node 
             
        return route
    
    def get_closest_node(self, start_node, avoid_visit_nodes, temp_dist_mat):
        for node in avoid_visit_nodes:
            temp_dist_mat[:,node.num] = 0
            
        row_num = start_node.num
        row = temp_dist_mat[row_num,:]
        
        minval = np.min(row[np.nonzero(row)])
        min_index = np.where(row == minval)[0][0]
        end_node = self.node_list[min_index]
        
        return end_node
    
    def get_route_distance(self, route):
        distance = 0
        for i in range(1, len(route)):
            distance += route[i-1].distance(route[i])
            
        return distance
        
    def plot_routes(self, route):
        for i in range(1, len(route)):
            x_values = [route[i-1].x, route[i].x]
            y_values = [route[i-1].y, route[i].y]
            
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
    
    def __init__(self, dist_mat, node_list, edge_list):
        super().__init__(dist_mat, node_list, edge_list)
        
        NN_routes = []
        for start_node in self.node_list:
            route = super().nearest_neighbour_route(start_node)
            route_distance = super().get_route_distance(route)
            NN_routes.append([route, route_distance])
            
        self.best_NN_route = min(NN_routes, key = lambda x: x[1])[0]
        self.NN_min_distance = min(NN_routes, key = lambda x: x[1])[1]
            
        self.MST_edges, self.MST_nodes = super().MST_tree()
        self.MST_distance = self.get_MST_distance()
        

class RouteGreedy(Route):
    
    def __init__(self, dist_mat, node_list, edge_list):
        super().__init__(dist_mat, node_list, edge_list)
        
        self.greedy_edges, self.greedy_nodes = self.greedy_route()
        
        
    def greedy_route(self):
        greedy_nodes = []
        greedy_edges = []
        self.available_edges = sorted(self.edge_list.copy())
        
        edge_queue = queue.Queue()
        for edge in self.available_edges:
            edge_queue.put(edge)
     
        while edge_queue.empty() == False:
            
            edge = edge_queue.get()
            print(edge)
            # not edge.creates_a_cycle(greedy_nodes)
            
            if (len(edge.node1.connected_edges) < 2
                and len(edge.node2.connected_edges) < 2
                and not RouteGreedy.creates_a_cycle(edge, greedy_edges)):
                
        
                
                greedy_edges.append(edge)
                edge.node1.connected_edges.append(edge)
                edge.node2.connected_edges.append(edge)
                
                if edge.node1 not in greedy_nodes:
                    greedy_nodes.append(edge.node1)
                if edge.node2 not in greedy_nodes:
                    greedy_nodes.append(edge.node2)
                    
       
                
        return greedy_edges, greedy_nodes   
    
    
    def plot_Greedy(self):
        for edge in self.greedy_edges:
            x_values = [edge.node1.x, edge.node2.x]
            y_values = [edge.node1.y, edge.node2.y]
            
            plt.plot(x_values, y_values)
        plt.title('Greedy')
        plt.show()
        
        
    def creates_a_cycle(edge, greedy_edges):
        temp_greedy_edges = greedy_edges.copy()
        temp_greedy_edges.append(edge)
        start = edge.node1
        
        return RouteGreedy.depthFirstTraversal(start, temp_greedy_edges)
    
    def depthFirstTraversal(start, temp_greedy_edges):
        graph = RouteGreedy.create_graph(temp_greedy_edges)
        stack = [start]
        visited = [start]
        while stack:
            current = stack.pop(-1)
            print(current)
            for elem in graph[current]:
                if elem not in visited:
                    stack.append(elem)
                else:
                    return False
        return True

    
    @staticmethod
    def create_graph(edges):
        graph = {}
        
        for edge in edges:
            if edge.node1 not in graph:
                graph[edge.node1] = []
            if edge.node2 not in graph:
                graph[edge.node2] = []
            
            graph[edge.node1].append(edge.node2)
            graph[edge.node2].append(edge.node1)
        
        return graph
           
          
            
        
        
        
        
        
        
        
    
       
       
        
         

              
    
    
    
        
             
    
     
        
