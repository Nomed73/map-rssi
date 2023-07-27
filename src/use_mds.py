import numpy as np
import data_sets as d
from matplotlib import pyplot as plt
import pprint as p

def create_matrix(data, targets):
  matrix = []
  length = len(targets)

  for r in range(0, length):
    row = []
    for c in range(0, length):
      p1 = targets[r]
      p2 = targets[c]
      
      for d in range(0, len(data)):
        if p1 == data[d]['keys'][0]:
          if p2 == data[d]['keys'][1]:
            row.append(data[d]['rssi'])
            break
        elif p2 == data[d]['keys'][0]:
          if p1 == data[d]['keys'][1]:
            row.append(data[d]['rssi'])
            break            
        elif p1 == p2:
          row.append(0)   
          break           
      
    matrix.append(row)
    np.matrix = matrix
  print(type(np.matrix))
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in np.matrix]))
  return np.matrix

def unique_targets(data):
  unique_targets = []
  for i in range(0, len(data)):
    if data[i]['keys'][0] not in unique_targets:
      unique_targets.append(data[i]['keys'][0])
    if data[i]['keys'][1] not in unique_targets:
      unique_targets.append(data[i]['keys'][1])
  
  return unique_targets




#------------- MAIN ------------------#

data = d.test01
targets = unique_targets(data)
print(f"targets = {targets}")
matrix = create_matrix(data, targets)