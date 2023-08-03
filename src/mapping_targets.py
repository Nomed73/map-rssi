import data_sets as d
import initiate_targets as it
import calculations as calc
from matplotlib import pyplot as plt

import pprint

def main(data_set):

    data = data_set
    unique_targets = it.unique_targets(data)
    targets = it.initiate_targets(unique_targets)
    targets = it.set_targets_rssi(targets, data)

    targets = calc.convert_rssi_inches(targets)
    targets = calc.first_two_targets(targets)
    pprint.pprint(targets)
    for i in range(2, len(targets)):
        targets = calc.distances(targets, i)
    map_targets(targets)


def map_targets(targets):
  x_plots = []
  y_plots = []
  label = []
  for i in range(0, len(targets)):
    x_plots.append(targets[i]['x'])
    y_plots.append(targets[i]['y'])
    label.append(f"Target {i + 1} - {targets[i]['current_target'][12:]}\n({targets[i]['x']:.1f}, {targets[i]['y']:.1f})")
  
  # Plotting
  plt.scatter(x_plots, y_plots)
  plt.axis('equal')
  plt.title('Targets')
  plt.grid(True)
  for i, txt, in enumerate(label):
    plt.annotate(txt, xy=(x_plots[i], y_plots[i]))
  plt.show()


if __name__=="__main__":
    main(d.test07)