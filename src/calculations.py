import numpy as np


def convert_rssi_inches(targets):
  mp = -36
  n = 2.75
  for i in range(0, len(targets)):
    exp_curr_next = (mp - (-1*targets[i]['rssi'])) / (10 * n)
    exp_curr_first = (mp - (-1*targets[i]['dist_to_first'])) / (10 * n)
    targets[i]['rssi'] = (10**exp_curr_next) * 39.3701
    targets[i]['dist_to_first'] = (10**exp_curr_first) * 39.3701
  return targets

def first_two_targets(targets):
    targets[0]['x'] = 0
    targets[0]['y'] = 0
    
    targets[1]['x'] = 0
    targets[1]['y'] = targets[0]['rssi']

    return targets

def rest_of_targets(targets):
    for i in range(2, len(targets)):
       pass

    return targets

def distances(targets, i):
  # for i in range(1, len(targets)):
  theta = np.linspace(0, 2 * np.pi, 100)
  targets[i]['x_list'] = targets[i-1]['rssi'] * np.cos(theta) + targets[i-1]['x']
  targets[i]['y_list'] = targets[i-1]['rssi'] * np.sin(theta) + targets[i-1]['y']

  targets[i]['possible_dist_to_first']=[]

  for j in range(0,len(targets[i]['x_list'])):
    distance = np.sqrt(targets[i]['x_list'][j]**2 + targets[i]['y_list'][j]**2)
    targets[i]['possible_dist_to_first'].append(distance)
  
  targets = find_target_center(targets, i)
  return targets

def find_target_center(targets, index):
  closest_value = min(targets[index]['possible_dist_to_first'], key=lambda x: abs(targets[index]['dist_to_first'] - x))
  location = targets[index]['possible_dist_to_first'].index(closest_value)
  targets[index]['x'] = targets[index]['x_list'][location]
  targets[index]['y'] = targets[index]['y_list'][location]

  print(f"possible distances : {targets[index]['possible_dist_to_first']}")
  print(f"index of closest distance: {location}")
  print(f"closest value : {closest_value}")

  return targets

#return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]