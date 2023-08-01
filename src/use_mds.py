import numpy as np
import data_sets as d
import matplotlib.pyplot as plt
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
            # row.append(convert_rssi_inches(data[d]['rssi']))
            row.append(data[d]['rssi'])
            # break
        elif p2 == data[d]['keys'][0]:
          if p1 == data[d]['keys'][1]:
            # row.append(convert_rssi_inches(data[d]['rssi']))
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

def convert_rssi_inches(rssi):
  mp = -70
  n = 2
  exponent = (mp - (-1*rssi)) / (10 * n)
  inches = (10**exponent) * 39.3701
  return inches

def unique_targets(data):
  unique_targets = []
  for i in range(0, len(data)):
    if data[i]['keys'][0] not in unique_targets:
      unique_targets.append(data[i]['keys'][0])
    if data[i]['keys'][1] not in unique_targets:
      unique_targets.append(data[i]['keys'][1])
  
  return unique_targets

def mds_classic(distances, dimensions=2):
    # Square distances
    M = -0.5 * np.power(distances, 2)

    # Double center the rows/columns
    def mean(A):
        return np.add.reduce(A) / A.shape[0]
    
    row_means = mean(M)
    col_means = mean(M.T)
    total_mean = mean(row_means)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i][j] += total_mean - row_means[i] - col_means[j]

    # Take the SVD of the double-centered matrix and return the points from it
    U, S, Vt = np.linalg.svd(M)
    eigen_values = np.sqrt(S)
    # return np.multiply(U[:, :dimensions], eigen_values[:dimensions])
    return [np.multiply(row, eigen_values)[:dimensions] for row in U]

def plot_targets(target_locations):
  
  # Extract x and y coordinates from the array
  x_plot = [point[0] for point in target_locations]
  y_plot = [point[1] for point in target_locations]

  plt.plot(x_plot, y_plot, 'X')
  # plt.scatter(x = x_plot, y = y_plot)
  plt.grid(True)
  plt.title('Targets')
  for i, point in enumerate(target_locations):
    # plt.text(point[0], point[1], f'Point {i+1}', ha='right', va='bottom')
    plt.text(point[0], point[1], f'Point {i+1} ({point[0]:.2f}, {point[1]:.2f})', ha='right', va='bottom')
  
  plt.show()

#------------- MAIN ------------------#

data = d.test01
targets = unique_targets(data)
print(f"targets = {targets}")
matrix = create_matrix(data, targets)
target_locations = mds_classic(matrix)
print(f"type of target_locations = {type(target_locations)}")
print(target_locations)
plot_targets(target_locations)


####  Convert rssi to distances