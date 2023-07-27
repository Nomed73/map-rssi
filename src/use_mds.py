import numpy as np
import data_sets as d
from matplotlib import pyplot as plt
import pprint as p

def create_matrix(data, targets):
  matrix = []
  for i in range(0, len(targets)):
    row = []
    curr_row = targets[i]
    for j in range(0, len(targets)):
      curr_col = targets[j]
      if curr_col == curr_row:
        row.append(0)
      for d in range(0, len(data)):

        if curr_col in data[d]['keys'] and curr_row in data[d]['keys']:
          row.append(data[d]['rssi'])
          # del data[d]
          # break
      
    matrix.append(row)
    np.matrix = matrix
  print(type(np.matrix))
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in np.matrix]))

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
create_matrix(data, targets)