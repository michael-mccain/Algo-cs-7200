### Imports ###
from pathlib import Path
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
        final_dict.update({x[0] : x[1:(len(x))]})

    return int(match_int), final_dict

### MAIN ### 
def main():
    ### Variables ### 
    # Path Variables
    in_file = Path(__file__).parent / 'Input.txt'
    out_path = Path(__file__).parent
    out_file = out_path / 'Output.txt'

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
        

    
    proposals = {m: [] for m in proposer_dict} # keeps track of women already being proposed to
    engaged = {} # keeps track of which woman is engaged to which man

    while unmatched_proposers: # While there is a man m who is free and hasn’t proposed to
    # every woman w for which (m, w) ~F
        m = unmatched_proposers.pop(0)  # Choose such a man m 
                                         # w = 1st woman on m's list to whom m has not yet proposed if (w is free)
                                         # Chooses first on the list and takes it out
        for w in proposer_dict[m]:
            if w not in proposals[m]: # if the woman has not yet been proposed to
                proposals[m].append(w)  # mark as proposed
                if w not in engaged:      # woman is free
                    engaged[w] = m # assign m and w to be engaged
                else:                        # woman is engaged
                    current = engaged[w]
                    # If she prefers someone else 
                    # else if (w prefers m to her fiancé m')
                    if proposee_dict[w].index(m) < proposee_dict[w].index(current):
                        engaged[w] = m
                        unmatched_proposers.append(current)  # previous fiancé becomes free
                                                             # assign m and w to be engaged, and m' to be free
                    else:
                        unmatched_proposers.append(m)  # rejected, stay free
                                                       # else, w rejects m
                break  # move to next free man

    # Flip engaged to man->woman mapping
    matches = {m: w for w, m in engaged.items()}

    # Write Output.txt with number of matched as last line
    with open(out_file, 'w') as f:
        for m, w in matches.items():
            f.write(f"{m} {w}\n")
        f.write(f"{len(matches)}\n")



if __name__ == "__main__":
    main()