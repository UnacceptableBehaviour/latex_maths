#! /usr/bin/env python
# 3.7
# time complexity plot
# something not quite right - needs work

import time 
from numpy.random import seed 
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt 
import math
from pprint import pprint

from pathlib import Path

IMAGE_SCRATCH = Path('./scratch')    # scratch space not maintained by git
# NOTE to save jpg using matplotlib
#> pip install pillow
# plt.plot([1, 2])
# plt.savefig(IMAGE_SCRATCH.join('image.jpg'))

          
#     start = time.clock() 
#     algorithm_to_time(a) 
#     end = time.clock() 
#     print(len(a), "algorithm took ", end-start)


elements = []
cos = []
zero_2pow_zero = []

SCALE = 40.0

for n in range(0, 720):
    elements.append(n)    
    cos.append(math.cos(np.deg2rad(n)) * SCALE)

#float_range  = np.arange(1, 0.1, -0.1)
#float_range  = np.arange(1, 0.01, -0.01)
#float_range  = np.arange(1, 0.001, -0.001)
float_range  = np.arange(1, 0.0001, -0.0001)
float_range = [round(x, 4) for x in float_range]    # 4 decimal places is enough for fun!
pprint(float_range)

elements = []
for n in float_range:
    #print(n)
    elements.append(n)
    zero_2pow_zero.append(pow(n, n))    # pow(n,n) == n**n
    

plt.xlabel('n')               # elements
plt.ylabel('n ^ n')          # 
# plt.xscale('log')               # set x scale logarithmic
# plt.yscale('log')               # set y scale logarithmic

#plt.plot(elements, cos, label = "Graph of Cos (n deg to rads)")
plt.plot(elements, zero_2pow_zero, label="Limits n^n n->0 (zero ^ zero)")
plt.gca().invert_xaxis()


plt.grid() 
plt.legend()
print(Path.cwd())
plt.savefig( IMAGE_SCRATCH.joinpath('matplot_graph.jpg') )
plt.show()


# tidy up
# ticks = {1: [[0, 1.001],
#      [0, 1.001],
#      [0, 1.001],
#      [0, 1.0],
#      [0, 1.001],
#      [1, 1.001],
#      [0, 1.001],
#      [0, 1.0],
#      [0, 1.001],
#      [0, 1.001]],
#  2: [[0, 1.001],
#      [0, 0.501],
#      [0, 0.5],
#      [0, 0.5],
#      [0, 0.5],
#      [0, 0.501],
#      [0, 0.501],
#      [0, 0.5],
#      [0, 0.5],
#      [0, 0.502],
#      [0, 0.5]],
#  3: [[0, 0.501],
#      [0, 0.334],
#      [0, 0.334],
#      [0, 0.333],
#      [0, 0.333],
#      [0, 0.334],
#      [0, 0.333],
#      [0, 0.334],
#      [0, 0.332],
#      [0, 0.333],
#      [0, 0.333]],
#  4: [[0, 0.333],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.25],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.251],
#      [0, 0.251]],
#  5: [[0, 0.25],
#      [0, 0.201],
#      [0, 0.201],
#      [0, 0.2],
#      [0, 0.201],
#      [0, 0.2],
#      [0, 0.2],
#      [0, 0.2],
#      [0, 0.2],
#      [0, 0.2],
#      [0, 0.202]],
#  6: [[0, 0.201],
#      [0, 0.167],
#      [1, 0.166],
#      [1, 0.167],
#      [0, 0.167],
#      [0, 0.167],
#      [0, 0.166],
#      [1, 0.166],
#      [0, 0.166],
#      [0, 0.167],
#      [0, 0.166]],
#  7: [[0, 0.166],
#      [0, 0.143],
#      [0, 0.143],
#      [0, 0.142],
#      [0, 0.143],
#      [0, 0.142],
#      [0, 0.143],
#      [0, 0.143],
#      [0, 0.142],
#      [0, 0.143],
#      [0, 0.143]],
#  8: [[0, 0.142],
#      [0, 0.126],
#      [0, 0.126],
#      [0, 0.126],
#      [0, 0.126],
#      [0, 0.125],
#      [0, 0.125],
#      [0, 0.125],
#      [1, 0.127],
#      [0, 0.125],
#      [0, 0.126]],
#  9: [[0, 0.125],
#      [0, 0.112],
#      [0, 0.112],
#      [0, 0.112],
#      [0, 0.112],
#      [0, 0.112],
#      [0, 0.111],
#      [0, 0.113],
#      [0, 0.112],
#      [0, 0.111],
#      [0, 0.112]],
#  10: [[0, 0.112],
#       [0, 0.101],
#       [0, 0.1],
#       [0, 0.1],
#       [0, 0.101],
#       [0, 0.1],
#       [0, 0.101],
#       [0, 0.101],
#       [0, 0.101],
#       [0, 0.1],
#       [0, 0.101]],
#  20: [[0, 0.1],
#       [0, 0.05],
#       [0, 0.051],
#       [0, 0.051],
#       [0, 0.051],
#       [0, 0.05],
#       [0, 0.051],
#       [0, 0.05],
#       [0, 0.053],
#       [0, 0.05],
#       [0, 0.051]],
#  30: [[1, 0.051],
#       [0, 0.035],
#       [0, 0.033],
#       [0, 0.034],
#       [0, 0.034],
#       [0, 0.034],
#       [0, 0.033],
#       [0, 0.033],
#       [0, 0.034],
#       [0, 0.034],
#       [0, 0.032]],
#  40: [[0, 0.034],
#       [0, 0.025],
#       [0, 0.026],
#       [0, 0.026],
#       [0, 0.026],
#       [0, 0.025],
#       [0, 0.026],
#       [0, 0.025],
#       [0, 0.026],
#       [0, 0.026],
#       [0, 0.025]],
#  50: [[0, 0.026],
#       [0, 0.021],
#       [0, 0.02],
#       [0, 0.021],
#       [0, 0.02],
#       [1, 0.02],
#       [0, 0.021],
#       [0, 0.02],
#       [0, 0.021],
#       [0, 0.02],
#       [0, 0.02]],
#  60: [[0, 0.02],
#       [0, 0.018],
#       [0, 0.016],
#       [0, 0.017],
#       [0, 0.016],
#       [0, 0.016],
#       [0, 0.017],
#       [0, 0.016],
#       [0, 0.017],
#       [0, 0.017],
#       [0, 0.017]],
#  70: [[0, 0.016],
#       [0, 0.014],
#       [0, 0.015],
#       [0, 0.015],
#       [0, 0.014],
#       [0, 0.014],
#       [0, 0.014],
#       [0, 0.015],
#       [0, 0.015],
#       [0, 0.016],
#       [0, 0.016]],
#  80: [[0, 0.017],
#       [0, 0.016],
#       [0, 0.018],
#       [0, 0.016],
#       [0, 0.016],
#       [0, 0.018],
#       [0, 0.016],
#       [0, 0.017],
#       [0, 0.016],
#       [0, 0.017],
#       [0, 0.016]],
#  90: [[0, 0.017],
#       [0, 0.018],
#       [0, 0.016],
#       [0, 0.015],
#       [0, 0.019],
#       [0, 0.016],
#       [0, 0.018],
#       [0, 0.017],
#       [0, 0.016],
#       [0, 0.016],
#       [0, 0.017]],
#  100: [[0, 0.018],
#        [0, 0.015],
#        [1, 0.017],
#        [0, 0.017],
#        [0, 0.017],
#        [0, 0.016],
#        [0, 0.016],
#        [0, 0.018],
#        [0, 0.017],
#        [0, 0.017],
#        [0, 0.017]]}


# {10: [[1000, 0],
#       [1000, 100],
#       [1000, 101],
#       [1000, 101],
#       [1000, 101],
#       [1000, 100],
#       [1000, 101],
#       [1000, 100],
#       [1000, 101],
#       [1000, 101],
#       [1000, 101],
#       [2000, 102],
#       [2000, 100],
#       [2000, 101],
#       [2000, 100],
#       [2000, 100],
#       [2000, 101],
#       [2000, 101],
#       [2000, 100],
#       [2000, 100],
#       [2000, 101],
#       [2000, 101],
#       [3000, 100],
#       [3000, 100],
#       [3000, 100],
#       [3000, 100],
#       [3000, 102],
#       [3000, 99],
#       [3000, 101],
#       [3000, 100],
#       [3000, 100],
#       [3000, 101],
#       [3000, 100],
#       [4000, 101],
#       [4000, 101],
#       [4000, 100],
#       [4000, 102],
#       [4000, 101],
#       [4000, 100],
#       [4000, 101],
#       [4000, 100],
#       [4000, 110],
#       [4000, 101],
#       [4000, 101],
#       [5000, 101],
#       [5000, 109],
#       [5000, 103],
#       [5000, 107],
#       [5000, 109],
#       [5000, 118],
#       [5000, 135],
#       [5000, 107],
#       [5000, 109],
#       [5000, 115],
#       [5000, 112],
#       [6000, 113],
#       [6000, 133],
#       [6000, 129],
#       [6000, 127],
#       [6000, 127],
#       [6000, 147],
#       [6000, 143],
#       [6000, 140],
#       [6000, 152],
#       [6000, 147],
#       [6000, 132],
#       [8000, 127],
#       [8000, 167],
#       [8000, 170],
#       [8000, 174],
#       [8000, 171],
#       [8000, 174],
#       [8000, 178],
#       [8000, 174],
#       [8000, 177],
#       [8000, 170],
#       [8000, 192],
#       [9000, 186],
#       [9000, 214],
#       [9000, 224],
#       [9000, 233],
#       [9000, 269],
#       [9000, 416],
#       [9000, 232],
#       [9000, 242],
#       [9000, 262],
#       [9000, 207],
#       [9000, 222],
#       [10000, 202],
#       [10000, 221],
#       [10000, 224],
#       [10000, 225],
#       [10000, 234],
#       [10000, 217],
#       [10000, 213],
#       [10000, 223],
#       [10000, 225],
#       [10000, 217],
#       [10000, 215]]}
# 
# 
