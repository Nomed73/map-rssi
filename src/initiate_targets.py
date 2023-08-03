
def unique_targets(data):
  unique_targets = []
  for i in range(0, len(data)):
    if data[i]['keys'][0] not in unique_targets:
      unique_targets.append(data[i]['keys'][0])
    if data[i]['keys'][1] not in unique_targets:
      unique_targets.append(data[i]['keys'][1])

  return unique_targets

def initiate_targets(unique_targets):
  targets = []
  for i in range(0, len(unique_targets)):
    target= { 
              'label':unique_targets[i][12:],
              'current_target': unique_targets[i], 
            }
    if i == len(unique_targets) - 1:
      target['next_target'] = unique_targets[0] 
    else: 
      target['next_target'] =  unique_targets[i + 1] 
        
    targets.append(target)
  return targets

def set_targets_rssi(targets, data):
  for i in range(0, len(targets)):
    for d in range(0, len(data)):
      if  targets[i]['current_target'] == data[d]['keys'][0] or targets[i]['current_target'] == data[d]['keys'][1]:
        if targets[i]['next_target'] == data[d]['keys'][0] or targets[i]['next_target'] == data[d]['keys'][1]:
          targets[i]['rssi'] = data[d]['rssi']
      if i == 0:
        targets[i]['dist_to_first'] = 0
      else: 
        if targets[0]['current_target'] in data[d]['keys'] and targets[i]['current_target'] in data[d]['keys']:
          targets[i]['dist_to_first'] = data[d]['rssi']

     
  return targets