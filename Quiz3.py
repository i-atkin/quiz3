#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:15:05 2021

@author: i_atkin
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
from mpl_toolkits.mplot3d import Axes3D

h5_file = h5py.File("test_ssx_particle_trajectory.h5", 'r')

# Look at the structure whithin the file 
print(h5_file.keys())

# Assign to local variable

position = h5_file['r'][()]

# Close the file 
h5_file.close()
# Plotting using local variables


# Create a 3D axis object
ax = plt.gcf().add_subplot(111, projection='3d')

# Make a plot of a trajectory given x, y, and z arrays as a function of time
ax.plot(position[:,0], position[:,1], position[:,2])
plt.title("Particle Trajectory 3D Plot")

# Export Plot 
plt.savefig('particletrajectory_plot.pdf')  