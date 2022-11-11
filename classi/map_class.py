# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:46:01 2022

@author: DSL1PVI
"""
import numpy as np
import matplotlib.pyplot as plt
import math   
import itertools


from classi.route_class import RouteNN, RouteGreedy

# # rng = np.random.default_rng()
rng = np.random.default_rng(seed = 12345)



class Node:
    
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.connected_edges = []
        self.connected_nodes = []
        
    def __repr__(self):
        return f"node:{self.num} x:{self.x} y:{self.y} n_edges: {len(self.connected_edges)}"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __hash__(self):
        return hash((self.num, self.x, self.y))
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
    
        

class Edge:
    
    def __init__ (self, num, node1, node2):
        self.num = num
        self.node1 = node1
        self.node2 = node2
        self.edge_len = node1.distance(node2)
        
    def __repr__(self):
        return f"edge:{self.num} {self.node1} {self.node2} edge_len={self.edge_len: .2f}\n"
    
    def __gt__(self, other):
        return self.edge_len > other.edge_len
    
    def __eq__(self, other):
        return self.num == other.num
    
    def __contains__(self, node):
        if node == self.node1 or node == self.node2:
            return True
        return False
    
    def __add__(self, other):
        return self.edge_len + other.edge_len
    
    
    def contains_nodes(self, list_of_nodes):
        for node in list_of_nodes:
            if node == self.node1 or node == self.node2:
                return True 
        return False
    
    def contains_exactly_one_node(self, list_of_nodes):
        count = 0
        for node in list_of_nodes:
            if  node == self.node1 or node == self.node2:
                count += 1
        if count == 1:
            return True
        else:
            return False
        
    def creates_a_cycle(self, list_of_nodes):
        if self.node1 in list_of_nodes and self.node2 in list_of_nodes:
            return True
        return False
    

    
                      

class Map:
    
    
    def __init__(self, map_name, num_points, max_x, max_y):
        self.map_name = map_name
        self.num_points = num_points
        self.map_max_x = max_x
        self.map_max_y = max_y
        self.node_list = []
    
    @property
    def num_points(self):
        return self._num_points
    
    @num_points.setter
    def num_points(self, value):
        if value <= 0:
            raise ValueError("num points must be > zero")
        self._num_points = value
    
    def __len__(self):
        return len(self.node_list)
    
    def __str__(self):
        return f"{self.map_name}, num_nodi:{self.num_points}"
        
    def generate_grid_random(self):
        x_values = rng.integers(low=0, high=self.map_max_x, size=self.num_points)
        y_values = rng.integers(low=0, high=self.map_max_y, size=self.num_points)
        self.grid = np.column_stack((x_values, y_values))
        
    def plot_grid(self):
        # fig=plt.figure(1)
        fig, ax = plt.subplots()
        x = self.grid[:,0]
        y = self.grid[:,1]
        ax=fig.add_axes([0,0,1,1])
        nodes_num = [i for i in range(0, len(self.grid[:,0]))]
        ax.scatter(x, y, color='r')
        for i in nodes_num:
            ax.annotate(i, (x[i], y[i]))
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
        
        self.dist_mat = self.dist_mat + np.transpose(self.dist_mat)
        
    def closest_neighbour(self):
        return RouteNN(self.dist_mat, self.node_list, self.edge_list) 
    
    def greedy(self):
        return RouteGreedy(self.dist_mat, self.node_list, self.edge_list) 
        
   
        
        
    