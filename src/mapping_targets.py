import data_sets as data
import data_handler as dh
import pprint

def main():
    unique_targets = dh.unique_targets(data.test01)
    targets = dh.initiate_targets(unique_targets)
    pprint.pprint(unique_targets)
    pprint.pprint(targets)

if __name__=="__main__":
    main()