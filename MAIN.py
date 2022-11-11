# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:44:55 2022

@author: DSL1PVI
"""
import numpy as np
from classi.map_class import Map
import statistics


np.random.seed(123)


mappa1 = Map('mappa1', 10, 50, 50)
mappa1.generate_grid_random()
mappa1.plot_grid()
mappa1.generate_nodes()
mappa1.generate_edges()
#mappa1.plot_edges()
mappa1.create_distance_matrix()


distances = []
routes = []

for start_node in range(0, 3):
    route_NN = mappa1.closest_neighbour(mappa1.node_list[start_node])
    route_NN.plot_routes()
    route_NN.plot_MST()
    distances.append(route_NN.route_distance)
    routes.append(route_NN)
    

print(f"media: {statistics.mean(distances)}")
print(f"MST: {route_NN.MST_distance}")
