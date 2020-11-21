#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:50:19 2020

@author: jixingman
"""

# these line up better with the 1D memoization table K
item_weights = [3, 2, 4, 3]
item_values = [2, 3, 3, 2]

n = len(item_weights)
W = 10 # total weight capacity
K = [0] * (W + 1)

# Base case redundant, but added for clarity
K[0] = 0

# Recurrence
for w in range(1, W + 1):
  max_sub_result = 0
  for i in range(1, n):
    wi = item_weights[i]
    vi = item_values[i]
    if wi <= w:
      subproblem_value = K[w - wi] + vi
      if subproblem_value > max_sub_result:
        max_sub_result = subproblem_value 
  K[w] = max_sub_result

# Results
print("Result: ", K[W])
print("K array: ", K)