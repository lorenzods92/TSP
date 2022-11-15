# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:44:55 2022

@author: DSL1PVI
"""
import numpy as np
from classi.map_class import Map
from classi.route_class import RouteNN, RouteGreedy
import statistics


np.random.seed(123)


mappa1 = Map('mappa1', 25, 50, 50)
mappa1.generate_grid_random()
mappa1.plot_grid()
mappa1.generate_nodes()
mappa1.generate_edges()
mappa1.create_distance_matrix()


distances = []
routes = []


route_NN = mappa1.closest_neighbour(mappa1.node_list[0])
route_NN.plot_routes(route_NN.route)
route_NN.plot_MST()

route_G = mappa1.greedy(mappa1.node_list[0])
route_G.plot_Greedy()

print(f" NN: {route_NN.route_distance}")
print(f" GREEDY: {route_G.route_distance}")


    

