import data_sets as d


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
    if i == len(unique_targets) - 1:
      target = {  
                  'p1': unique_targets[i],
                  'p2': unique_targets[0]
      }
    else:
      target = {  
                  'p1': unique_targets[i],
                  'p2': unique_targets[i + 1]
      }
    targets.append(target)
  return targets