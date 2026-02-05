### Imports ###
from pathlib import Path
from operator import itemgetter
import itertools

### Variables ### 
# Path Variables
in_file = Path(__file__).parent / 'Input.txt'
out_path = Path(__file__).parent

# Other variables
name_dict = {} # Intialized list of all names
proposer_dict = {} # Intialized list of propser preference
proposee_dict = {}  # Initilaized list of propsee preference
unmatched_proposers = [] # Initlaized List of matched propsers 

### MAIN ### 
## Read in file to populate dictionaries and lists
line_count = 0
with open(in_file, 'r') as file:
    next(file)
    lines = file.read()
    names = lines.strip().split('\n')

    for name in names: # Populate name dictionary
        x = name.split(' ')
        propser = itemgetter(0)
        name_dict.update({propser(x) : ""})

line_count = (len(x) - 1)
proposer_dict = dict(itertools.islice(name_dict.items(), 0, line_count)) # populate proposer dictionary (Men)
proposee_dict = dict(itertools.islice(name_dict.items(), line_count,len(name_dict))) # Populate propsee dictionary (Ladies)

for key in proposer_dict.keys():    # Populate unmatched list for while condition
    unmatched_proposers.append(key) 

# While there is a man m who is free and hasn’t proposed to
# every woman w for which (m, w) ~F
