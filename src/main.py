

import numpy as np
# import data_set_02 as d
import data_sets as d
from matplotlib import pyplot as plt
import pprint


def log(targets, msg):
  print(f"*************** {msg} ***************")
  for i in range(0, len(targets)):
    print(f"INDEX = {i} ")
    print(f"\tcenter: {targets[i]['center']}")
    print(f"\tnext target: {targets[i]['next_target']}")
    print(f"\tx : {targets[i]['x']}")
    print(f"\ty : {targets[i]['y']}")
    print(f"\tradius : {targets[i]['radius']}")

'''----------------------------------------
  Name: get_data()

  @remarks:
    Reads the data and returns a sorted list of dictionaries. 

  @params
    none
    
  @returns
    Sorted list of dictionaries based on the rssi value, least to greatest
'''
def get_data(test): 
  data = prep_data(test)
  # data = convert_rssi_inches(data)
  return sorted(data, key=lambda d: d['rssi'])


def prep_data(test):
  targets = []
  for i in range(0, len(test)):
    target = {
                'id': test[i]['id'],
                'p1': test[i]['keys'][0],
                'p2': test[i]['keys'][1],
                'rssi':test[i]['rssi']
    }
    targets.append(target)
  return targets


def convert_rssi_inches(data):
  mp = -36
  n = 2.75
  for i in range(0, len(data)):
    exponent = (mp - (-1*data[i]['rssi'])) / (10 * n)
    inches = (10**exponent) * 39.3701
    data[i]['rssi'] = inches
  return data


'''----------------------------------------
  Name: set_first_two()

  @remarks:
    Determines which are the first two targets that are placed. The first one is placed
    at (0,0) and the second one is placed at (0,y).

  @params
    data  : sorted data list. 
    index : 0 or 1, depending  on if it is the first or second target that will be placed. 

  @returns
    Dictionary storing all the target information needed for finding other points and creating plot
'''
def set_first_two(data, index):
  print("func: set_first_two")
  if index == 0:
    target = {
              'center' : data[index]['p1'],
              'x' : 0,
              'y' : 0, 
              'next_target': data[index]['p2'],
              'radius': data[index]['rssi'],
              'distance_to_origin': 0, 
              'used': True 
            }

  elif index == 1:
    center =  data[index - 1]['p2']
    dto = data[index-1]['rssi']#dist_to_center(data, data[index - 1]['p2'], data[index]['p2'] )
    np = next_target(data, center, targets)
    radius = dist_to_center( data, center, np )
    target = {
              'center' : center,
              'x' : 0,
              'y' : data[0]['rssi'], 
              'next_target': np, 
              'radius': radius,
              'distance_to_origin': dto,  
              'used': True
            } 
    
  return target 


'''----------------------------------------
  Name: rest_of_targets()

  @remarks:
    Determine the location and placement of targets after the first two are set

  @params
    data    : Original data list
    targets : List of targets
    index   : The index in the targets list to work on 

  @returns
    None
'''
def rest_of_targets(data, targets, index, last):
  print("func: rest_of_targets")
  center = targets[index-1]['next_target']
  if (index == last - 1 ):
    next = data[0]['p1']
  else:
    next = next_target(data, center, targets)

  dto = dist_to_center(data, data[0]['p1'], next)
  radius = dist_to_center( data, center, next )
  
  target = {
          'center' : center,
          'next_target': next, 
          'radius': radius,
          'distance_to_origin': dto,  
          'used': True
        } 
  return target
  # gen_xy_values(targets, index)
  # targets = find_xy(targets, index)


def find_xy(targets, index):
  print("func: find_xy")
  closest_value = min(targets[index]['points_on_circle'], key=lambda x: abs(targets[index-1]['distance_to_origin'] - x))
  location = targets[index]['points_on_circle'].index(closest_value)
  targets[index]['x'] = targets[index]['x_list'][location]
  targets[index]['y'] = targets[index]['y_list'][location]
  log(targets, "Inside find_xy before the return")
  return targets
  # msg = f"find_xy : index = {index} "
  # log(targets, msg)


'''----------------------------------------
  Name: dist_to_center()

  @remarks:
    

  @params
    data    : Original data list
    p1      :
    p2      : 

  @returns
    None
'''
def dist_to_center(data, p1, p2):
   print("func: distance_to_center")
   for i in range (0, len(data)):
      if (( p1 == data[i]['p1'] and p2 == data[i]['p2']) or 
          ( p2 == data[i]['p1'] and p1 == data[i]['p2'])):
        return data[i]['rssi']


'''----------------------------------------
  Name: gen_xy_values()

  @remarks:
    Generates x.y pairs on the perimeter of the rssi value. These values will determine
    the center for the next perimeter.

  @params
    targets : List of targets
    index   : The index in the targets list to work on 

  @returns
    None
 
'''
def gen_xy_values(targets, index):
  print("func: generate_xy_values")

  theta = np.linspace(0, 2 * np.pi, 100)
  targets[index]['x_list'] = targets[index]['radius'] * np.cos(theta) + targets[index-1]['x']
  targets[index]['y_list'] = targets[index]['radius'] * np.sin(theta) + targets[index-1]['y']

  targets[index]['points_on_circle']=[]
  for i in range(0,len(targets[index]['x_list'])):
    distance = np.sqrt(targets[index]['x_list'][i]**2 + targets[index]['y_list'][i]**2)
    targets[index]['points_on_circle'].append(distance)

  return targets

'''----------------------------------------
  Name: next_target()

  @remarks
    

  @params

  @returns
 
'''
def next_target(data, center, targets):
  print("func: next_target")
  used_targets = []
  for t in range(0, len(targets)-1):
    if targets[t]['used'] == True:
      used_targets.append(targets[t]['center'])

  for i in range(1, len(data)):
    if ( center not in used_targets and ( center == data[i]['p1'] or center == data[i]['p2'] ) ):
      if (center == data[i]['p1'] and center != data[i]['p2']):
          return data[i]['p2']
      if (center == data[i]['p2'] and center != data[i]['p1']):
        return data[i]['p1']  
      


  # if (center == data[0]['p1']):
  return data[0]['p1']

'''----------------------------------------
  Name: map_targets()

  @remarks
    

  @params

  @returns
    None
'''
def map_targets(targets):
  print('func: plot_the_targets')

  x_plots = []
  y_plots = []
  label = []
  for i in range(0, len(targets)):
    x_plots.append(targets[i]['x'])
    y_plots.append(targets[i]['y'])
    label.append(f"Target {i + 1} - {targets[i]['center'][12:]}\n({targets[i]['x']:.1f}, {targets[i]['y']:.1f})")
  
  # Plotting
  plt.scatter(x_plots, y_plots)
  plt.axis('equal')
  plt.title('Targets')
  for i, txt, in enumerate(label):
    plt.annotate(txt, xy=(x_plots[i], y_plots[i]))
  plt.show()


# ---------------- MAIN ---------------------# 

#Get the sorted data, sort is by rssi. smallest to largest. 
data = get_data(d.test01)

# Determine the number of targets based on the data
# Data provided has rssi values between all targets
coeff = [1, -1, -2*len(data)]
roots = np.roots(coeff)
for root in roots:
  if root > 0:
    number_targets = int(root)

# Get the location of the targets
targets = []
targets.append(set_first_two(data, 0))
targets.append(set_first_two(data, 1))
targets = gen_xy_values(targets, 1)
# targets = find_xy(targets, 1)

for i in range (2, number_targets):
  msg = f"i = {i}: For loop"
  log(targets, msg)
  target = rest_of_targets(data, targets, i, number_targets)
  targets.append(target)

  targets = gen_xy_values(targets, i)
  targets = find_xy(targets, i)
  
#Create plot of target locations
map_targets(targets)

