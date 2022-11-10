# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:44:55 2022

@author: DSL1PVI
"""

# import numpy as np
# import matplotlib.pyplot as plt
# import math   
# import itertools

from classi.map_class import Map



mappa1 = Map('mappa1', 6, 50, 50)
mappa1.generate_grid_random()
mappa1.plot_grid()
mappa1.generate_nodes()
mappa1.generate_edges()
mappa1.plot_edges()
mappa1.create_distance_matrix()



mappa1.closest_neighbour(mappa1.node_list[3])