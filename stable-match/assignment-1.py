### Imports ###
from pathlib import Path
from operator import itemgetter
import itertools

### Functions ###
# Read input file, return dictionary and integer from first line 
def read_file(in_file):
    final_dict = {}
    with open(in_file, 'r') as file:
        match_int = file.readline().strip()
        lines = file.read()
        names = lines.strip().split('\n')

    for name in names: # Populate name dictionary
        x = name.split(' ')
        propser = itemgetter(0)
        final_dict.update({propser(x) : x[1:(len(x))]})

    return int(match_int), final_dict

### MAIN ### 
def main():
    ### Variables ### 
    # Path Variables
    in_file = Path(__file__).parent / 'Input.txt'
    out_path = Path(__file__).parent

    # Other variables
    name_dict = {} # Intialized list of all names
    proposer_dict = {} # Intialized list of propser preference
    proposee_dict = {}  # Initilaized list of propsee preference
    unmatched_proposers = [] # Initlaized List of matched propsers 
    match_count = 0

    # Read Input.txt to get dictionary and match count
    match_count, name_dict = read_file(in_file)

    proposer_dict = dict(itertools.islice(name_dict.items(), 0, match_count)) # populate proposer dictionary (Men)
    proposee_dict = dict(itertools.islice(name_dict.items(), match_count,len(name_dict))) # Populate propsee dictionary (Ladies)

    # print('Men: ', proposer_dict)
    # print('Women: ', proposee_dict)

    for key in proposer_dict.keys():    # Populate unmatched list for while condition
        unmatched_proposers.append(key) 

    # While there is a man m who is free and hasn’t proposed to
    # every woman w for which (m, w) ~F

if __name__ == "__main__":
    main()